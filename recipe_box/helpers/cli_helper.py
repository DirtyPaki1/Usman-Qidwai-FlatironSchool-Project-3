import json
from models.recipe import Recipe

def display_menu():
    print("\nRecipe Box App")
    print("----------------")
    print("1. View Recipes")
    print("2. Add New Recipe")
    print("3. Delete Recipe")
    print("4. View Ingredients")
    print("5. Add New Ingredient")
    print("6. Delete Ingredient")
    print("7. Exit")

def get_recipe_input():
    title = input("Enter recipe title: ")
    description = input("Enter recipe description: ")
    category = input("Enter recipe category: ")
    return title, description, category

def get_ingredient_input():
    name = input("Enter ingredient name: ")
    quantity = float(input("Enter quantity: "))
    unit = input("Enter unit: ")
    return name, quantity, unit

def display_recipes(recipes):
    print("\nRecipes:")
    if recipes is None:
        print("No recipes found.")
        return
    for i, recipe in enumerate(recipes, 1):
        print(f"{i}. {recipe.title} - Category: {recipe.category}")

def display_ingredients(ingredients):
    print("\nIngredients:")
    if ingredients is None:
        print("No ingredients found.")
        return
    for i, ingredient in enumerate(ingredients, 1):
        print(f"{i}. {ingredient.name} ({ingredient.quantity} {ingredient.unit})")

def main():
    recipes = []
    
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            display_recipes(recipes)
        elif choice == "2":
            title, description, category = get_recipe_input()
            new_recipe = Recipe.create(title, description, category)
            recipes.append(new_recipe)
            print(f"Added new recipe: {new_recipe.title}")
        elif choice == "3":
            if not recipes:
                print("No recipes to delete.")
            else:
                display_recipes(recipes)
                recipe_id = int(input("Enter recipe ID to delete: ")) - 1
                if 0 <= recipe_id < len(recipes):
                    del recipes[recipe_id]
                    print("Recipe deleted successfully!")
                else:
                    print("Invalid recipe ID.")
        elif choice == "4":
            print("Ingredients feature not implemented yet.")
        elif choice == "5":
            print("Ingredients feature not implemented yet.")
        elif choice == "6":
            print("Ingredients feature not implemented yet.")
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
