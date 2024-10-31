from lib.database import create_tables, get_connection
from lib.models.actor import Actor
from lib.models.movie import Movie

def main_menu():
    while True:
        print("\n--- Movie and Actor Management ---")
        print("1. Manage Movies")
        print("2. Manage Actors")
        print("3. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            manage_movies()
        elif choice == '2':
            manage_actors()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_movies():
    while True:
        print("\n--- Manage Movies ---")
        print("1. Add Movie")
        print("2. Delete Movie")
        print("3. View All Movies")
        print("4. View Actors in Movie")
        print("5. Go Back")

        choice = input("Select an option: ")
        
        if choice == '1':
            title = input("Enter movie title: ")
            year = int(input("Enter movie year: "))
            movie = Movie(title=title, year=year)
            movie.save()
            print(f"Movie '{movie.title}' added.")
        elif choice == '2':
            title = input("Enter movie title to delete: ")
            movie = Movie.find_by_title(title)
            if movie:
                movie.delete()
                print(f"Movie '{title}' deleted.")
            else:
                print(f"Movie '{title}' not found.")
        elif choice == '3':
            movies = Movie.get_all()
            for movie in movies:
                print(movie.form())
        elif choice == '4':
            title = input("Enter movie title to view actors: ")
            movie = Movie.find_by_title(title)
            if movie:
                actors = movie.get_actors()
                for actor in actors:
                    print(actor.form())
            else:
                print(f"Movie '{title}' not found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

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
            actor = Actor(name=name, age=age, movie_title=movie_title)
            actor.save()
            print(f"Actor '{actor.name}' added.")
        elif choice == '2':
            name = input("Enter actor name to delete: ")
            actor = Actor.find_by_name(name)
            if actor:
                actor.delete()
                print(f"Actor '{name}' deleted.")
            else:
                print(f"Actor '{name}' not found.")
        elif choice == '3':
            actors = Actor.get_all()
            for actor in actors:
                print(actor.form())
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    create_tables()  # Create tables before running the CLI
    main_menu()
