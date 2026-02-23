import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("SPOONACULAR_API_KEY")
BASE_URL = "https://api.spoonacular.com/recipes"

def search_recipes(ingredients, diet=None, number=6):
    """Search recipes based on ingredients and dietary filters."""
    endpoint = f"{BASE_URL}/complexSearch"
    params = {
        "apiKey": API_KEY,
        "includeIngredients": ",".join(ingredients),
        "diet": diet,
        "fillIngredients": True,
        "addRecipeInformation": True,
        "number": number,
        "sort": "min-missing-ingredients" # Prioritize recipes with fewer missing items
    }
    
    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        return response.json().get("results", [])
    except Exception as e:
        print(f"Error fetching recipes: {e}")
        return []

def get_recipe_details(recipe_id):
    """Fetch full instructions and data for a specific recipe."""
    endpoint = f"{BASE_URL}/{recipe_id}/information"
    params = {"apiKey": API_KEY}
    
    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching details: {e}")
        return None