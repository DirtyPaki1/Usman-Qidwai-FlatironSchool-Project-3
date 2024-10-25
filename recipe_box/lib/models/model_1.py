# lib/models/model_1.py

import os
import json
from datetime import date, time

class Category:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.recipes = []

    def __repr__(self):
        return f"Category(id={self.id}, name='{self.name}')"

class Recipe:
    def __init__(self, id, title, description, category_id):
        self.id = id
        self.title = title
        self.description = description
        self.category_id = category_id
        self.category = None

    def __repr__(self):
        return f"Recipe(id={self.id}, title='{self.title}', description='{self.description}', category_id={self.category_id})"

def create_category(categories, name):
    new_category = Category(len(categories) + 1, name)
    categories.append(new_category)
    return new_category

def delete_category(categories, category_id):
    for i, category in enumerate(categories):
        if category.id == category_id:
            del categories[i]
            return
    raise ValueError(f"No category found with id {category_id}")

def get_all_categories(categories):
    return categories

def get_category_by_name(categories, name):
    for category in categories:
        if category.name.lower() == name.lower():
            return category
    return None

def create_recipe(recipes, title, description, category_id):
    new_recipe = Recipe(len(recipes) + 1, title, description, category_id)
    recipes.append(new_recipe)
    return new_recipe

def delete_recipe(recipes, recipe_id):
    for i, recipe in enumerate(recipes):
        if recipe.id == recipe_id:
            del recipes[i]
            return
    raise ValueError(f"No recipe found with id {recipe_id}")

def get_all_recipes(recipes):
    return recipes

def get_recipe_by_id(recipes, recipe_id):
    for recipe in recipes:
        if recipe.id == recipe_id:
            return recipe
    return None

def get_recipes_by_category(recipes, category_id):
    return [recipe for recipe in recipes if recipe.category_id == category_id]

def save_to_db(categories, recipes):
    os.makedirs('data', exist_ok=True)
    os.makedirs('data/categories', exist_ok=True)
    os.makedirs('data/recipes', exist_ok=True)
    
    categories_file = 'data/categories.json'
    recipes_file = 'data/recipes.json'

    # Save categories
    with open(categories_file, 'w') as f:
        json.dump([{'id': c.id, 'name': c.name} for c in categories], f)
    
    # Save recipes
    with open(recipes_file, 'w') as f:
        json.dump([{'id': r.id, 'title': r.title, 'description': r.description, 'category_id': r.category_id} for r in recipes], f)

def load_from_db():
    os.makedirs('data', exist_ok=True)
    os.makedirs('data/categories', exist_ok=True)
    os.makedirs('data/recipes', exist_ok=True)
    
    categories_file = 'data/categories.json'
    recipes_file = 'data/recipes.json'

    try:
        with open(categories_file, 'r') as f:
            categories = [Category(**cat) for cat in json.load(f)]
        
        with open(recipes_file, 'r') as f:
            recipes = [Recipe(**rec) for rec in json.load(f)]
    
    except FileNotFoundError:
        # Create empty lists if files don't exist
        categories = []
        recipes = []

    return categories, recipes
