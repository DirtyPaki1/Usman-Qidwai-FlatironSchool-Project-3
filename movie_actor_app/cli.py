from lib import initialize_tables
from lib.models.movie import Movie
from lib.models.actor import Actor
from lib.helpers import display_menu, validate_integer_input

def main_menu():
    initialize_tables()  # Create tables at the start
    while True:
        display_menu(["Manage Movies", "Manage Actors", "Exit"])
        choice = input("Choose an option: ").strip()

        if choice == '1':
            manage_movies()
        elif choice == '2':
            manage_actors()
        elif choice == '3':  # Exit option
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

def manage_movies():
    while True:
        display_menu(["Add Movie", "View All Movies", "Delete Movie", "View Movie's Actors", "Back"])
        choice = input("Choose an option: ").strip()

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
            movies = Movie.get_all()
            if not movies:
                print("No movies found.")
            else:
                for i, movie in enumerate(movies, start=1):
                    print(f"{i}. {movie.title} ({movie.year})")
                movie_title = input("Enter the title of the movie to delete: ").strip()
                movie = next((m for m in movies if m.title.lower() == movie_title.lower()), None)
                if movie:
                    movie.delete()
                    print(f"Movie '{movie.title}' and its associated actors deleted.")
                else:
                    print("Movie not found.")
        elif choice == '4':
            movie_title = input("Enter the title of the movie to view associated actors: ").strip()
            movie = next((m for m in Movie.get_all() if m.title.lower() == movie_title.lower()), None)
            if movie:
                actors = movie.get_actors()
                if actors:
                    for i, actor in enumerate(actors, start=1):
                        print(f"{i}. {actor.name}, Age: {actor.age}")
                else:
                    print("No actors associated with this movie.")
            else:
                print("Movie not found.")
        elif choice == '5':  # Back option
            break
        else:
            print("Invalid choice. Please try again.")

def manage_actors():
    while True:
        display_menu(["Add Actor", "View All Actors", "Delete Actor", "Back"])
        choice = input("Choose an option: ").strip()

        if choice == '1':
            name = input("Enter actor name: ").strip()
            age = validate_integer_input("Enter actor age: ", min_value=0)
            movies = Movie.get_all()
            if not movies:
                print("No movies found. Please add a movie before adding actors.")
                continue

            print("Available Movies:")
            for i, movie in enumerate(movies, start=1):
                print(f"{i}. {movie.title} ({movie.year})")
                
            movie_title = input("Enter the title of the movie the actor belongs to: ").strip()
            movie = next((m for m in movies if m.title.lower() == movie_title.lower()), None)
            if not movie:
                print("Movie not found. Cannot add actor to a non-existent movie.")
                continue
            
            try:
                Actor.create(name, age, movie)
                print(f"Actor '{name}' added to movie '{movie.title}'.")
            except ValueError as e:
                print(e)
                
        elif choice == '2':
            actors = Actor.get_all()
            if not actors:
                print("No actors found.")
            else:
                for i, actor in enumerate(actors, start=1):
                    print(f"{i}. {actor.name}, Age: {actor.age}")
        elif choice == '3':
            actor_name = input("Enter the name of the actor to delete: ").strip()
            actor = next((a for a in Actor.get_all() if a.name.lower() == actor_name.lower()), None)
            if actor:
                actor.delete()
                print(f"Actor '{actor.name}' deleted.")
            else:
                print("Actor not found.")
        elif choice == '4':  # Back option
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
