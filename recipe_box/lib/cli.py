# lib/cli.py

from models.model_1 import Category, Recipe, create_category, delete_category, get_all_categories, \
    get_category_by_name, create_recipe, delete_recipe, get_all_recipes, get_recipe_by_id, \
    get_recipes_by_category, save_to_db, load_from_db
from datetime import date, time
from helpers import validate_input, get_float_input, get_date_input, get_time_input

class CLI:
    def __init__(self):
        self.categories, self.recipes = load_from_db()

    def display_menu(self):
        print("\n--- Recipe Box CLI ---")
        print("1. View Categories")
        print("2. Add Category")
        print("3. Delete Category")
        print("4. View Recipes")
        print("5. Add Recipe")
        print("6. Delete Recipe")
        print("7. Search Recipes")
        print("8. Exit")

    def view_categories(self):
        if self.categories:
            print("\nCategories:")
            for category in self.categories:
                print(f"{category.id}. {category.name}")
        else:
            print("No categories found.")

    def add_category(self):
        name = validate_input("Enter category name: ").strip()
        if not name:
            print("Category name cannot be empty.")
            return
        try:
            new_category = create_category(self.categories, name)
            print(f"Category '{new_category.name}' added successfully.")
            save_to_db(self.categories, self.recipes)
        except Exception as e:
            print(f"Error adding category: {str(e)}")

    def delete_category(self):
        if not self.categories:
            print("No categories to delete.")
            return
        category_id = int(input("Enter category ID to delete: "))
        try:
            delete_category(self.categories, category_id)
            print("Category deleted successfully.")
            save_to_db(self.categories, self.recipes)
        except ValueError as e:
            print(str(e))

    def view_recipes(self):
        if self.recipes:
            print("\nRecipes:")
            for recipe in self.recipes:
                print(f"{recipe.id}. {recipe.title} ({recipe.category_name})")
        else:
            print("No recipes found.")

    def add_recipe(self):
        if not self.categories:
            print("Please add a category first.")
            return
        category_id = validate_input("Enter category ID: ", int)
        title = validate_input("Enter recipe title: ").strip()
        if not title:
            print("Recipe title cannot be empty.")
            return
        description = validate_input("Enter recipe description: ").strip()
        if not description:
            print("Recipe description cannot be empty.")
            return
        try:
            new_recipe = create_recipe(self.recipes, title, description, category_id)
            print(f"Recipe '{new_recipe.title}' added successfully.")
            save_to_db(self.categories, self.recipes)
        except ValueError:
            print("Invalid category ID. Please choose a valid category.")

    def delete_recipe(self):
        if not self.recipes:
            print("No recipes to delete.")
            return
        recipe_id = int(input("Enter recipe ID to delete: "))
        try:
            delete_recipe(self.recipes, recipe_id)
            print("Recipe deleted successfully.")
            save_to_db(self.categories, self.recipes)
        except ValueError as e:
            print(str(e))

    def search_recipes(self):
        if not self.recipes:
            print("No recipes to search.")
            return
        search_term = input("Search by recipe name or ingredient: ").strip().lower()
        matching_recipes = [
            recipe for recipe in self.recipes
            if search_term in recipe.title.lower() or search_term in recipe.description.lower()
        ]
        if matching_recipes:
            print("\nMatching recipes:")
            for recipe in matching_recipes:
                print(f"{recipe.id}. {recipe.title} ({recipe.category_name})")
        else:
            print("No matching recipes found.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-8): ")
            if choice == '1':
                self.view_categories()
            elif choice == '2':
                self.add_category()
            elif choice == '3':
                self.delete_category()
            elif choice == '4':
                self.view_recipes()
            elif choice == '5':
                self.add_recipe()
            elif choice == '6':
                self.delete_recipe()
            elif choice == '7':
                self.search_recipes()
            elif choice == '8':
                print("Saving changes...")
                save_to_db(self.categories, self.recipes)
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please choose again.")

if __name__ == "__main__":
    cli = CLI()
    cli.run()
