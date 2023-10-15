import openai
import json
from dotenv import load_dotenv
import os

load_dotenv()


import openai
import json
from dotenv import load_dotenv
import os

load_dotenv()


def generate_diet_plan(age: int, gender: str, height: int, weight: int, dietary_preferences: str, fitness_goals: str, food_allergies: str) -> dict:
    """
    Generate a diet plan using OpenAI GPT-3.
    
    Args:
        age (int): The age of the person.
        gender (str): The gender of the person.
        height (int): The height of the person in cm.
        weight (int): The weight of the person in kg.
        dietary_preferences (str): The dietary preferences of the person.
        fitness_goals (str): The fitness goals of the person.
        food_allergies (str): The food allergies of the person.
        
    Returns:
        dict: A dictionary containing the meal plan.
    """
    prompt = f"Generate a diet plan for a {age}-year-old {gender} who is {height} cm tall and weighs {weight} kg. They have the following dietary preferences: {dietary_preferences}, fitness goals: {fitness_goals}, food allergies: {food_allergies}. Return in json format like [{{'meal_type': 'breakfast', 'meal_items': []}},{{'meal_type': 'lunch', 'meal_items': []}}, {{'meal_type': 'snack', 'meal_items': []}}, {{'meal_type': 'dinner', 'meal_items': []}}]"

    completion = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
        api_key=os.getenv("API_KEY"),
    )

    message = completion.choices[0].text.strip()

    return {"meal_plan": message}
    

    completion = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
        api_key=os.getenv("API_KEY"),
    )

    message = completion.choices[0].text.strip()
    #print(' -- message -- ',message,type(message))
    #output_plan= json.dumps(message, indent=4)
    #print(' -- output_plan -- ',output_plan,type(output_plan))

    return {"meal_plan": message}
    
