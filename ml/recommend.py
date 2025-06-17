def calculate_bmi(weight_kg: float, height_cm: float) -> float:
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

def classify_bmi(bmi: float) -> str:
    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= bmi < 24.9:
        return "normal"
    elif 25 <= bmi < 29.9:
        return "overweight"
    else:
        return "obese"

def recommend_diet(bmi_category: str, goal: str = "maintain") -> dict:
    meal_plan = {
        "underweight": {
            "gain": [
                "Breakfast: Peanut butter toast + banana shake",
                "Lunch: Rajma rice + paneer",
                "Dinner: Veg pulao + dal + curd"
            ]
        },
        "normal": {
            "maintain": [
                "Breakfast: Oats with fruits",
                "Lunch: Brown rice + dal + salad",
                "Dinner: Chapati + sabzi + curd"
            ]
        },
        "overweight": {
            "loss": [
                "Breakfast: Boiled egg whites + oats",
                "Lunch: Grilled chicken + quinoa",
                "Dinner: Veg soup + multigrain bread"
            ]
        },
        "obese": {
            "loss": [
                "Breakfast: Green smoothie + boiled eggs",
                "Lunch: Grilled tofu + salad",
                "Dinner: Soup + steamed vegetables"
            ]
        }
    }

    return {
        "category": bmi_category,
        "goal": goal,
        "meals": meal_plan.get(bmi_category, {}).get(goal, [])
    }
