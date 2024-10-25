# main.py
from models.recipe import Recipe
from models.ingredient import Ingredient
from helpers.cli_helper import main as cli_main

def run_app():
    print("Welcome to the Recipe Box App!")
    cli_main()

if __name__ == "__main__":
    run_app()
