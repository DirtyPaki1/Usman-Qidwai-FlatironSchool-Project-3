import inquirer
from lib.models.movie import Movie
from lib.models.actor import Actor

def main_menu():
    while True:
        choices = ["Manage Movies", "Manage Actors", "Exit"]
        question = [inquirer.List("choice", message="Select an option", choices=choices)]
        choice = inquirer.prompt(question)["choice"]

        if choice == "Manage Movies":
            movie_menu()
        elif choice == "Manage Actors":
            actor_menu()
        elif choice == "Exit":
            break

def movie_menu():
    choices = ["Create Movie", "Delete Movie", "View All Movies", "Find Movie by ID", "Back"]
    question = [inquirer.List("choice", message="Select an option", choices=choices)]
    choice = inquirer.prompt(question)["choice"]

    try:
        if choice == "Create Movie":
            title = input("Enter movie title: ")
            release_year = int(input("Enter release year: "))
            Movie.create(title, release_year)
            print("Movie created successfully!")
        elif choice == "Delete Movie":
            movie_id = int(input("Enter movie ID to delete: "))
            Movie.delete(movie_id)
            print("Movie deleted successfully!")
        elif choice == "View All Movies":
            print(Movie.get_all())
        elif choice == "Find Movie by ID":
            movie_id = int(input("Enter movie ID to find: "))
            print(Movie.find_by_id(movie_id))
        elif choice == "Back":
            return
    except Exception as e:
        print(f"Error: {e}")

def actor_menu():
    choices = ["Create Actor", "Delete Actor", "View All Actors", "Find Actor by ID", "Back"]
    question = [inquirer.List("choice", message="Select an option", choices=choices)]
    choice = inquirer.prompt(question)["choice"]

    try:
        if choice == "Create Actor":
            name = input("Enter actor name: ")
            age = int(input("Enter actor age: "))
            movie_id = int(input("Enter associated movie ID: "))
            Actor.create(name, age, movie_id)
            print("Actor created successfully!")
        elif choice == "Delete Actor":
            actor_id = int(input("Enter actor ID to delete: "))
            Actor.delete(actor_id)
            print("Actor deleted successfully!")
        elif choice == "View All Actors":
            print(Actor.get_all())
        elif choice == "Find Actor by ID":
            actor_id = int(input("Enter actor ID to find: "))
            print(Actor.find_by_id(actor_id))
        elif choice == "Back":
            return
    except Exception as e:
        print(f"Error: {e}")
