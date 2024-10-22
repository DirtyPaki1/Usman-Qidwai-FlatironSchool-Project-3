from .models import Recipe, Ingredient

def create_recipe(title, description, cuisine, difficulty, cooking_time):
    return Recipe(title, description, cuisine, difficulty, cooking_time)

def delete_recipe(recipe):
    Recipe.all_recipes().remove(recipe)
    for ing in recipe.ingredients:
        ing.remove_from_recipe(recipe)
    for step in recipe.steps:
        recipe.remove_step(recipe.steps.index(step))
    for tag in recipe.tags:
        recipe.remove_tag(tag)

def display_all_recipes():
    for recipe in Recipe.all_recipes():
        print(f"{recipe.id}: {recipe.title}")
        print(f"Cuisine: {recipe.cuisine}, Difficulty: {recipe.difficulty}")
        print(f"Cooking Time: {recipe.cooking_time} minutes")
        print("Ingredients:")
        for ing in recipe.ingredients:
            print(f"- {ing.name}: {ing.quantity} {ing.unit}")
        print("Steps:")
        for i, step in enumerate(recipe.steps, 1):
            print(f"{i}. {step}")
        print("Tags:", ", ".join(recipe.tags))
        print("---")

def find_recipe_by_title(title):
    for recipe in Recipe.all_recipes():
        if title.lower() in recipe.title.lower():
            return recipe
    return None

def create_ingredient(name, quantity, unit):
    return Ingredient(name, quantity, unit)

def delete_ingredient(ingredient):
    Ingredient.all_ingredients().remove(ingredient)
    for recipe in ingredient.recipes:
        recipe.remove_ingredient(ingredient)

def display_all_ingredients():
    for ing in Ingredient.all_ingredients():
        print(f"{ing.id}: {ing.name}")

def find_ingredient_by_name(name):
    for ing in Ingredient.all_ingredients():
        if name.lower() in ing.name.lower():
            return ing
    return None
