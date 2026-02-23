import json
import os

DB_FILE = "data/favorites.json"

def load_favorites():
    if not os.path.exists(DB_FILE):
        os.makedirs("data", exist_ok=True)
        with open(DB_FILE, "w") as f:
            json.dump([], f)
        return []
    
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_favorite(recipe):
    favorites = load_favorites()
    # Avoid duplicates
    if not any(f['id'] == recipe['id'] for f in favorites):
        favorites.append(recipe)
        with open(DB_FILE, "w") as f:
            json.dump(favorites, f, indent=4)

def remove_favorite(recipe_id):
    favorites = load_favorites()
    favorites = [f for f in favorites if f['id'] != recipe_id]
    with open(DB_FILE, "w") as f:
        json.dump(favorites, f, indent=4)