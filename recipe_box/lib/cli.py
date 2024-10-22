import json

class Recipe:
    def __init__(self, title, description, cuisine, difficulty, cooking_time):
        self.title = title
        self.description = description
        self.cuisine = cuisine
        self.difficulty = difficulty
        self.cooking_time = cooking_time

class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

recipe_db = []
ingredient_db = []

def load_data():
    global recipe_db, ingredient_db
    try:
        with open("recipe_box.json", "r") as f:
            data = json.load(f)
        recipe_db = [Recipe(**r) for r in data["recipes"]]
        ingredient_db = [Ingredient(**i) for i in data["ingredients"]]
    except FileNotFoundError:
        pass

def save_data():
    global recipe_db, ingredient_db
    data = {
        "recipes": [r.__dict__ for r in recipe_db],
        "ingredients": [i.__dict__ for i in ingredient_db]
    }
    with open("recipe_box.json", "w") as f:
        json.dump(data, f)

def create_recipe(title, description, cuisine, difficulty, cooking_time):
    return Recipe(title, description, cuisine, difficulty, cooking_time)

def delete_recipe(recipe):
    recipe_db.remove(recipe)

def find_recipe_by_title(title):
    for recipe in recipe_db:
        if title.lower() in recipe.title.lower():
            return recipe
    return None

def display_all_recipes():
    for recipe in recipe_db:
        print(f"Title: {recipe.title}")
        print(f"Cuisine: {recipe.cuisine}")
        print(f"Difficulty: {recipe.difficulty}")
        print(f"Cooking Time: {recipe.cooking_time} minutes")
        print("---")

def create_ingredient(name, quantity, unit):
    return Ingredient(name, quantity, unit)

def delete_ingredient(ingredient):
    ingredient_db.remove(ingredient)

def find_ingredient_by_name(name):
    for ingredient in ingredient_db:
        if name.lower() in ingredient.name.lower():
            return ingredient
    return None

def display_all_ingredients():
    for ingredient in ingredient_db:
        print(f"Name: {ingredient.name}, Quantity: {ingredient.quantity} {ingredient.unit}")

def main():
    load_data()

    while True:
        print("\nRecipe Box Menu:")
        print("1. Manage Recipes")
        print("2. Manage Ingredients")
        print("3. View All Recipes")
        print("4. View All Ingredients")
        print("5. Search for Recipe")
        print("6. Search for Ingredient")
        print("7. Save Data")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            while True:
                print("\nRecipe Options:")
                print("1. Add New Recipe")
                print("2. Delete Recipe")
                print("3. Back to Main Menu")
                
                sub_choice = input("Enter your choice (1-3): ")

                if sub_choice == '1':
                    title = input("Enter recipe title: ")
                    description = input("Enter recipe description: ")
                    cuisine = input("Enter cuisine type: ")
                    difficulty = input("Enter difficulty level: ")
                    cooking_time = int(input("Enter cooking time in minutes: "))
                    recipe = create_recipe(title, description, cuisine, difficulty, cooking_time)
                    recipe_db.append(recipe)
                elif sub_choice == '2':
                    title = input("Enter recipe title to delete: ")
                    recipe = find_recipe_by_title(title)
                    if recipe:
                        delete_recipe(recipe)
                    else:
                        print("Recipe not found.")
                elif sub_choice == '3':
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == '2':
            while True:
                print("\nIngredient Options:")
                print("1. Add New Ingredient")
                print("2. Delete Ingredient")
                print("3. Back to Main Menu")
                
                sub_choice = input("Enter your choice (1-3): ")

                if sub_choice == '1':
                    name = input("Enter ingredient name: ")
                    quantity = float(input("Enter quantity: "))
                    unit = input("Enter unit (e.g., cups, grams, etc.): ")
                    ingredient = create_ingredient(name, quantity, unit)
                    ingredient_db.append(ingredient)
                elif sub_choice == '2':
                    name = input("Enter ingredient name to delete: ")
                    ingredient = find_ingredient_by_name(name)
                    if ingredient:
                        delete_ingredient(ingredient)
                    else:
                        print("Ingredient not found.")
                elif sub_choice == '3':
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == '3':
            display_all_recipes()
        elif choice == '4':
            display_all_ingredients()
        elif choice == '5':
            title = input("Enter partial recipe title to search: ")
            result = find_recipe_by_title(title)
            if result:
                print(f"Found recipe: {result.title}")
            else:
                print("Recipe not found.")
        elif choice == '6':
            name = input("Enter partial ingredient name to search: ")
            result = find_ingredient_by_name(name)
            if result:
                print(f"Found ingredient: {result.name}, Quantity: {result.quantity} {result.unit}")
            else:
                print("Ingredient not found.")
        elif choice == '7':
            save_data()
            print("Data saved successfully.")
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()