def generate_shopping_list(favorites):
    """Aggregate missing ingredients from all favorite recipes."""
    shopping_list = []
    for recipe in favorites:
        # Missed ingredients are provided by the complexSearch response
        missed = recipe.get("missedIngredients", [])
        for item in missed:
            name = item.get("original")
            if name not in shopping_list:
                shopping_list.append(name)
    return shopping_list