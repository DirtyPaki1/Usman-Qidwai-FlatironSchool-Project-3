from lib.database import initialize_db
from lib.models.actor import Actor
from lib.models.movie import Movie
from lib.helpers import format_actor, format_movie


def main_menu():
    initialize_db()
    while True:
        print("\n--- Main Menu ---")
        print("1. Manage Movies")
        print("2. Manage Actors")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            manage_movies()
        elif choice == '2':
            manage_actors()
        elif choice == '3':
            print("Exiting application.")
            break
        else:
            print("Invalid option. Please try again.")


def manage_movies():
    while True:
        print("\n--- Manage Movies ---")
        print("1. Add Movie")
        print("2. View All Movies")
        print("3. Add Actor to Movie")
        print("4. Delete Actor from Movie")
        print("5. Delete Movie")
        print("6. Go Back")

        choice = input("Select an option: ")

        if choice == '1':
            title = input("Enter movie title: ")
            year = int(input("Enter movie year: "))
            movie = Movie(title=title, year=year)
            movie.save()
            print(f"Movie '{movie.title}' added.")

        elif choice == '2':
            movies = Movie.get_all()
            for movie in movies:
                print(format_movie(movie))
                actors = movie.get_actors()
                if actors:
                    for actor in actors:
                        print(f"  {format_actor(actor)}")
                else:
                    print("  No actors associated with this movie.")

        elif choice == '3':
            movie_title = input("Enter movie title to add actor to: ")
            movie = Movie.find_by_title(movie_title)
            if movie:
                name = input("Enter actor name: ")
                age = int(input("Enter actor age: "))
                actor = Actor(name=name, age=age, movie_id=movie.id)
                actor.save()
                print(f"Actor '{actor.name}' added to movie '{movie.title}'.")
            else:
                print("Movie not found.")

        elif choice == '4':
            movie_title = input("Enter movie title to delete actor from: ")
            movie = Movie.find_by_title(movie_title)
            if movie:
                actor_id = int(input("Enter actor ID to delete: "))
                Actor.delete(actor_id)
                print(f"Actor with ID {actor_id} deleted from movie '{movie.title}'.")
            else:
                print("Movie not found.")

        elif choice == '5':
            title = input("Enter movie title to delete: ")
            movie = Movie.find_by_title(title)
            if movie:
                movie.delete()
                print(f"Movie '{movie.title}' deleted along with its actors.")
            else:
                print("Movie not found.")

        elif choice == '6':
            break


def manage_actors():
    while True:
        print("\n--- Manage Actors ---")
        print("1. Add Actor")
        print("2. Delete Actor")
        print("3. View All Actors")
        print("4. Go Back")

        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter actor name: ")
            age = int(input("Enter actor age: "))
            movie_title = input("Enter associated movie title (optional): ")
            movie = Movie.find_by_title(movie_title) if movie_title else None
            movie_id = movie.id if movie else None
            
            actor = Actor(name=name, age=age, movie_id=movie_id)
            actor.save()
            print(f"Actor '{actor.name}' added.")

        elif choice == '2':
            actor_id = int(input("Enter actor ID to delete: "))
            Actor.delete(actor_id)
            print(f"Actor with ID {actor_id} deleted.")

        elif choice == '3':
            actors = Actor.get_all()
            for actor in actors:
                print(format_actor(actor))

        elif choice == '4':
            break


if __name__ == '__main__':
    main_menu()
