from lib.models.movie import Movie
from lib.models.actor import Actor

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Add Movie")
        print("2. Add Actor")
        print("3. View All Movies")
        print("4. View All Actors")
        print("5. View Actors for a Movie")
        print("6. Exit")

        choice = input("Select an option: ")
        if choice == "1":
            title = input("Enter movie title: ")
            try:
                year = int(input("Enter release year: "))
                movie = Movie(title, year)
                movie.save()
                print("Movie added successfully!")
            except ValueError as e:
                print(e)
        elif choice == "2":
            name = input("Enter actor's name: ")
            try:
                age = int(input("Enter actor's age: "))
                movie_id = input("Enter movie ID (leave blank if none): ")
                movie_id = int(movie_id) if movie_id else None
                actor = Actor(name, age, movie_id)
                actor.save()
                print("Actor added successfully!")
            except ValueError as e:
                print(e)
        elif choice == "3":
            movies = Movie.get_all()
            for movie in movies:
                print(movie)
        elif choice == "4":
            actors = Actor.get_all()
            for actor in actors:
                print(actor)
        elif choice == "5":
            movie_id = int(input("Enter movie ID to view actors: "))
            movie = Movie.find_by_id(movie_id)
            if movie:
                actors = movie.get_actors()
                print(f"Actors in {movie[1]}:")
                for actor in actors:
                    print(actor)
            else:
                print("Movie not found.")
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid option, please try again.")
