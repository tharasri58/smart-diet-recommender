from fastapi import FastAPI
from pydantic import BaseModel
from ml.recommend import calculate_bmi, classify_bmi, recommend_diet

app = FastAPI(title="Smart Diet Recommendation System")

# Define the expected input data using Pydantic
class UserInput(BaseModel):
    age: int
    gender: str
    height_cm: float
    weight_kg: float
    goal: str = "maintain"  # options: gain, maintain, loss

# Define the API endpoint
@app.post("/recommend")
def get_diet_plan(user: UserInput):
    bmi = calculate_bmi(user.weight_kg, user.height_cm)
    category = classify_bmi(bmi)
    diet = recommend_diet(category, user.goal)

    return {
        "bmi": bmi,
        "bmi_category": category,
        "goal": user.goal,
        "recommended_meals": diet["meals"]
    }

@app.get("/")
def read_root():
    return {"message": "Smart Diet API working!"}

@app.get("/bmi")
def get_bmi(weight: float, height: float):
    bmi = weight / (height ** 2)
    return {"bmi": round(bmi, 2)}

@app.post("/predict", response_model=DietResponse)
def get_recommendation(request: DietRequest):
    return recommend_diet(request)
