from lib.database import initialize_database
from lib.models.movie import Movie
from lib.models.actor import Actor
from lib.helpers import validate_string_input, validate_integer_input, display_objects

def main_menu():
    while True:
        print("\n=== Movie Actor Management ===")
        print("1. Manage Movies")
        print("2. Manage Actors")
        print("3. Exit")
        choice = validate_integer_input("Choose an option: ")

        if choice == 1:
            manage_movies()
        elif choice == 2:
            manage_actors()
        elif choice == 3:
            print("Exiting the application.")
            break
        else:
            print("Invalid option. Please try again.")

def manage_movies():
    while True:
        print("\n=== Manage Movies ===")
        print("1. Add Movie")
        print("2. Delete Movie")
        print("3. Show All Movies")
        print("4. Show Associated Actors")
        print("5. Back to Main Menu")
        choice = validate_integer_input("Choose an option: ")

        if choice == 1:
            title = validate_string_input("Enter movie title: ")
            year = validate_integer_input("Enter movie year: ")
            Movie.create(title, year)
            print(f"Movie '{title}' added successfully.")

        elif choice == 2:
            title = validate_string_input("Enter movie title to delete: ")
            Movie.delete(title)
            print(f"Movie '{title}' and its associated actors deleted successfully.")

        elif choice == 3:
            movies = Movie.get_all()
            display_objects(movies, "Movies")

        elif choice == 4:
            title = validate_string_input("Enter movie title to view associated actors: ")
            movie = Movie.find_by_title(title)
            if movie:
                actors = movie.get_associated_actors()
                display_objects(actors, f"Actors in '{title}'")
            else:
                print("Movie not found.")

        elif choice == 5:
            break

        else:
            print("Invalid option. Please try again.")

def manage_actors():
    while True:
        print("\n=== Manage Actors ===")
        print("1. Add Actor")
        print("2. Delete Actor")
        print("3. Show All Actors")
        print("4. Back to Main Menu")
        choice = validate_integer_input("Choose an option: ")

        if choice == 1:
            name = validate_string_input("Enter actor name: ")
            age = validate_integer_input("Enter actor age: ")
            movie_title = validate_string_input("Enter movie title for this actor: ")
            try:
                Actor.create(name, age, movie_title)
                print(f"Actor '{name}' added successfully.")
            except ValueError as e:
                print(e)

        elif choice == 2:
            name = validate_string_input("Enter actor name to delete: ")
            Actor.delete(name)
            print(f"Actor '{name}' deleted successfully.")

        elif choice == 3:
            actors = Actor.get_all()
            display_objects(actors, "Actors")

        elif choice == 4:
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    initialize_database()
    main_menu()
