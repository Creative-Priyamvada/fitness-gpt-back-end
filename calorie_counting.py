import openai
import json
import re
from dotenv import load_dotenv
import os

load_dotenv()



def get_food_info(food_name, food_quantity):
    """
    Get calorie value and nutrition information for a food item in JSON format.
    
    Args:
        food_name (str): The name of the food item.
        food_quantity (str): The quantity of the food item.
        
    Returns:
        str: A JSON string containing the calorie value and nutrition information for the food item.
    """
    prompt = f"Get calorie value and nutrition information for {food_quantity} of {food_name} in JSON format.  {{calorie:' ',nutrition :{{protein:,carbohydrates:,fat:,fiber:,sugar:,sodium:}}}}"


    completion = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
        api_key=os.getenv("API_KEY") 
,
    )

    message = completion.choices[0].text.strip()
    message = message.replace("'", '"')
    # Convert the returned string to a JSON object
    print(' -- message --',message)
    

    return str(message)