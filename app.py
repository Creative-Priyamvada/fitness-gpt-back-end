from flask import Flask, request, jsonify
from calorie_counting import get_food_info
from diet_plan import generate_diet_plan
from exercise_recommender import generate_exercise_recommendations

from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})



@app.route("/food_info", methods=["POST"])
def food_info():
    """
    Get calorie value and nutrition information for a food item.

    Request JSON:
    {
        "food_name": "string",
        "food_quantity": "string"
    }
    
    Response JSON:
    {
        "result": "string"
    }
    """
    data = request.json
    food_name = data.get("food_name")
    food_quantity = data.get("food_quantity", "")
    result = get_food_info(food_name, food_quantity)
    return jsonify(result=result)

@app.route("/diet_plan", methods=["POST"])
def diet_plan():
    """
    Generate a diet plan for a person.
    
    Request JSON:
    {
        "age": "integer",
        "gender": "string",
        "height": "integer",
        "weight": "integer",
        "dietary_preferences": "string",
        "fitness_goals": "string",
        "food_allergies": "string"
    }
    
    Response JSON:
    {
        "result": "string"
    }
    """
    data = request.json
    age = data.get("age")
    gender = data.get("gender")
    height = data.get("height")
    weight = data.get("weight")
    dietary_preferences = data.get("dietary_preferences")
    fitness_goals = data.get("fitness_goals")
    food_allergies = data.get("food_allergies")
    #current_diet = data.get("current_diet")

    result = generate_diet_plan(age, gender, height, weight, dietary_preferences, fitness_goals, food_allergies)
    return jsonify(result=result)

@app.route("/exercise_recommendations", methods=["POST"])
def exercise_recommendations():
    """
    Generate exercise recommendations for a person.
    
    Request JSON:
    {
        "age": "integer",
        "gender": "string",
        "height": "integer
        "weight": "integer",
    "daily_activity_levels": "string",
    "fitness_goals": "string",
    "lifestyle_factors": "string"
    }

    Response JSON:
    {
        "result": "string"
    }
    """
    data = request.json
    age = data.get("age")
    gender = data.get("gender")
    height = data.get("height")
    weight = data.get("weight")
    daily_activity_levels = data.get("daily_activity_levels")
    fitness_goals = data.get("fitness_goals")
    lifestyle_factors = data.get("lifestyle_factors")

    result = generate_exercise_recommendations(age, gender, height, weight, daily_activity_levels, fitness_goals, lifestyle_factors)
    return jsonify(result=result)

if __name__ == "__main__":
    app.run(debug=True,port=8001)
