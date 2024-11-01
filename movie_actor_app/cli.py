from lib import initialize_tables
from lib.models.movie import Movie
from lib.models.actor import Actor
from lib.helpers import display_menu, validate_integer_input

def main_menu():
    initialize_tables()  # Create tables at the start
    while True:
        display_menu(["Manage Movies", "Manage Actors", "Exit"])
        choice = input("Choose an option (1/2/3): ").strip()

        if choice == '1':
            manage_movies()
        elif choice == '2':
            manage_actors()
        elif choice == '3' or choice.lower() == 'exit':
            print("Exiting the application.")
            break  # Exit the loop and terminate the program
        else:
            print("Invalid choice. Please try again.")

def manage_movies():
    while True:
        display_menu(["Add Movie", "View All Movies", "Delete Movie", "View Movie's Actors", "Back"])
        choice = input("Choose an option (1/2/3/4/Back): ").strip()
        
        if choice == '1':
            title = input("Enter movie title: ").strip()
            year = validate_integer_input("Enter movie year: ", min_value=1888)
            try:
                Movie.create(title, year)
                print(f"Movie '{title}' added.")
            except ValueError as e:
                print(e)
        elif choice == '2':
            movies = Movie.get_all()
            if not movies:
                print("No movies found.")
            else:
                for i, movie in enumerate(movies, start=1):
                    print(f"{i}. {movie.title} ({movie.year})")
        elif choice == '3':
            movie_id = validate_integer_input("Enter movie ID to delete: ")
            movie = Movie.find_by_id(movie_id)
            if movie:
                # First delete all actors associated with this movie
                actors = Actor.get_all()
                for actor in actors:
                    if actor.movie_id == movie_id:
                        Actor.delete(actor.id)
                Movie.delete(movie_id)
                print(f"Movie '{movie.title}' and its associated actors deleted.")
            else:
                print("Movie not found.")
        elif choice == '4':
            title = input("Enter movie title to view associated actors: ").strip()
            movie = Movie.find_by_title(title)
            if movie:
                actors = Actor.get_all()
                associated_actors = [a for a in actors if a.movie_id == movie.id]
                if associated_actors:
                    for i, actor in enumerate(associated_actors, start=1):
                        print(f"{i}. {actor.name}, Age: {actor.age}")
                else:
                    print("No actors associated with this movie.")
            else:
                print("Movie not found.")
        elif choice.lower() == 'back':
            print("Returning to main menu...")
            break  # Go back to the main menu
        else:
            print("Invalid choice. Please try again.")

def manage_actors():
    while True:
        display_menu(["Add Actor", "View All Actors", "Delete Actor", "Back"])
        choice = input("Choose an option (1/2/3/Back): ").strip()
        
        if choice == '1':
            name = input("Enter actor name: ").strip()
            age = validate_integer_input("Enter actor age: ", min_value=0)
            movie_id = validate_integer_input("Enter movie ID the actor belongs to: ")
            try:
                Actor.create(name, age, movie_id)
                print(f"Actor '{name}' added.")
            except ValueError as e:
                print(e)
        elif choice == '2':
            actors = Actor.get_all()
            if not actors:
                print("No actors found.")
            else:
                for i, actor in enumerate(actors, start=1):
                    print(f"{i}. {actor.name}, Age: {actor.age}, Movie ID: {actor.movie_id}")
        elif choice == '3':
            actor_id = validate_integer_input("Enter actor ID to delete: ")
            actor = Actor.find_by_id(actor_id)
            if actor:
                Actor.delete(actor_id)
                print(f"Actor '{actor.name}' deleted.")
            else:
                print("Actor not found.")
        elif choice.lower() == 'back':
            print("Returning to main menu...")
            break  # Go back to the main menu
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
