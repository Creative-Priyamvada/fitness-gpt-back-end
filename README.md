# GPT-challenge-back-end

`pip install -r requirements.py`

`python app.py`

## Endpoint for diet plan

`http://localhost:8001/diet_plan`

example input :

```
{
    "age": 33,
    "gender": "Female",
    "height": "6'0''",
    "weight": 185,
    "health_status": "Good",
    "dietary_preferences": "Vegetarian",
    "fitness_goals": "Weight Loss",
    "food_allergies": "None",
    "current_diet": "Balanced",
}
```

## Endpoint for exercise recommendation

`http://localhost:8001/exercise_recommendations`

```
{
    "age": 30,
    "gender": "male",
    "height": 180,
    "weight": 80,
    "daily_activity_levels": "moderate",
    "fitness_goals": "lose weight",
    "lifestyle_factors": "sedentary"
}

```

## Endpoint for calorie counting

`http://localhost:8001/food_info`

```
{
    "food_name": "apple",
    "food_quantity": "1 medium"
}

```


