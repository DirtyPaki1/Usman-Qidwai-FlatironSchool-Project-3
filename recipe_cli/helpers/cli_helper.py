import sys

def fetch_recipes():
    # Simulating recipe fetching from an API
    return [
        {"id": 1, "name": "Spaghetti Bolognese", "description": "Classic Italian pasta dish"},
        {"id": 2, "name": "Chicken Tikka Masala", "description": "Popular Indian-inspired British curry"},
        {"id": 3, "name": "Roasted Vegetable Quinoa Bowl", "description": "Healthy and flavorful vegetarian bowl"}
    ]

def print_recipes(recipes=None):
    if recipes is None:
        print("Error: No recipes available.")
        return
    
    if not isinstance(recipes, list) or len(recipes) == 0:
        print("Error: Empty recipe list.")
        return
    
    print("Available recipes:")
    for i, rec in enumerate(recipes, 1):
        print(f"{i}. {rec['name']} - {rec['description']}")

def create_recipe(title, description, category_id):
    new_recipe = Recipe.create(title, description, category_id)
    # Save the new recipe to the database
    new_recipe.save()
    print(f"New recipe '{title}' created successfully.")

def delete_recipe(recipe_id):
    # Delete the recipe from the database
    Recipe.delete(recipe_id)
    print(f"Recipe with ID {recipe_id} deleted successfully.")

def get_all_recipes():
    all_recipes = Recipe.get_all()
    if not all_recipes:
        print("No recipes found.")
        return
    print("\nAll Recipes:")
    for recipe in all_recipes:
        print(f"- {recipe.title}")

def find_recipe_by_id(recipe_id):
    recipe = Recipe.find_by_id(recipe_id)
    if recipe:
        print(f"\nFound recipe:\n{recipe}")
    else:
        print(f"No recipe found with ID {recipe_id}")

def find_recipe_by_attribute(attribute, value):
    recipes = Recipe.find_by_attribute(attribute, value)
    if recipes:
        print(f"\nRecipes matching {attribute} = '{value}':")
        for recipe in recipes:
            print(f"- {recipe.title}")
    else:
        print(f"No recipes found matching {attribute} = '{value}'")

def main():
    while True:
        print("\nRecipe Box Menu:")
        print("1. View All Recipes")
        print("2. Find Recipe by ID")
        print("3. Find Recipe by Attribute")
        print("4. Create New Recipe")
        print("5. Delete Recipe")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            get_all_recipes()
        elif choice == '2':
            recipe_id = int(input("Enter recipe ID to find: "))
            find_recipe_by_id(recipe_id)
        elif choice == '3':
            attribute = input("Enter attribute to search (e.g., title, description): ").lower()
            value = input("Enter value to search for: ")
            find_recipe_by_attribute(attribute, value)
        elif choice == '4':
            title = input("Enter recipe title: ")
            description = input("Enter recipe description: ")
            category_id = input("Enter category ID: ")
            create_recipe(title, description, category_id)
        elif choice == '5':
            recipe_id = int(input("Enter recipe ID to delete: "))
            delete_recipe(recipe_id)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
