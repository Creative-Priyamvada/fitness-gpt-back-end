import json
import os
import re

import openai
from dotenv import load_dotenv

load_dotenv()


def parse_exercise_recommendations(message: str) -> list:
    """
    Parse the exercise recommendations from the OpenAI GPT-3 response message.
    
    Args:
        message (str): The response message from OpenAI GPT-3.
        
    Returns:
        list: A list of dictionaries containing exercise recommendations.
    """
    pattern = r"'exercise_name': '(.*?)', 'description': \[(.*?)\]"
    matches = re.findall(pattern, message)
    result_list = []

    for match in matches:
        exercise_name = match[0]
        description = match[1].split(", ")
        description = [desc.strip("'") for desc in description]
        result_list.append({"exercise_name": exercise_name, "description": description})

    return result_list


def generate_exercise_recommendations(age: int, gender: str, height: int, weight: int, daily_activity_levels: str, fitness_goals: str, lifestyle_factors: str) -> str:
    """
    Generate exercise recommendations using OpenAI GPT-3.
    
    Args:
        age (int): The age of the person.
        gender (str): The gender of the person.
        height (int): The height of the person in cm.
        weight (int): The weight of the person in kg.
        daily_activity_levels (str): The daily activity level of the person.
        fitness_goals (str): The fitness goals of the person.
        lifestyle_factors (str): The lifestyle factors of the person.
        
    Returns:
        str: A JSON string containing exercise recommendations.
    """
    prompt = f"A {age}-year-old {gender} who is {height} cm tall and weighs {weight} kg, has a daily activity level of {daily_activity_levels} and the following fitness goals: {fitness_goals}. They lead a {lifestyle_factors} lifestyle. Recommend exercises for them in format [{{'exercise_name': ' ', 'description': []}},{{'exercise_name': ' ', 'description': []}}, {{'exercise_name': ' ', 'description': []}}, {{'exercise_name': ' ', 'description': []}}]"

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
    parsed=parse_exercise_recommendations(message)
    json_string = json.dumps(parsed)
    return str(json_string)
