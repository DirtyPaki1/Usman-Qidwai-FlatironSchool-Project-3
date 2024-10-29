import sys
from lib.models.movie import Movie
from lib.models.actor import Actor

def display_menu():
    print("\n1. Add Movie")
    print("2. View All Movies")
    print("3. Add Actor")
    print("4. View All Actors")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("Select an option: ")
        
        if choice == '1':
            title = input("Enter movie title: ")
            release_year = int(input("Enter release year: "))
            movie = Movie(title, release_year)
            movie.save()
            print("Movie added.")
        
        elif choice == '2':
            movies = Movie.get_all()
            print("\nMovies:")
            for m in movies:
                print(f"ID: {m[0]}, Title: {m[1]}, Release Year: {m[2]}")
        
        elif choice == '3':
            name = input("Enter actor name: ")
            age = int(input("Enter actor age: "))
            movie_id = input("Enter movie ID (or leave blank): ")
            actor = Actor(name, age, movie_id if movie_id else None)
            actor.save()
            print("Actor added.")
        
        elif choice == '4':
            actors = Actor.get_all()
            print("\nActors:")
            for a in actors:
                print(f"ID: {a[0]}, Name: {a[1]}, Age: {a[2]}, Movie ID: {a[3]}")
        
        elif choice == '5':
            print("Exiting...")
            sys.exit()
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
