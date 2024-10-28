# lib/cli.py

import sys
from lib.models.movie import Movie
from lib.models.actor import Actor

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Manage Movies")
        print("2. Manage Actors")
        print("3. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            movie_menu()
        elif choice == "2":
            actor_menu()
        elif choice == "3":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

def movie_menu():
    while True:
        print("\nMovie Menu:")
        print("1. Add Movie")
        print("2. View All Movies")
        print("3. Find Movie by ID")
        print("4. Delete Movie")
        print("5. Go Back")

        choice = input("Choose an option: ")
        if choice == "1":
            add_movie()
        elif choice == "2":
            display_movies()
        elif choice == "3":
            find_movie_by_id()
        elif choice == "4":
            delete_movie()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def add_movie():
    title = input("Enter movie title: ")
    try:
        release_year = int(input("Enter release year: "))
        movie = Movie(title, release_year)
        movie.save()
        print(f"Movie '{title}' added successfully.")
    except ValueError as e:
        print(e)

def display_movies():
    movies = Movie.get_all()
    for movie in movies:
        print(f"{movie[1]} ({movie[2]})")

def find_movie_by_id():
    movie_id = int(input("Enter movie ID: "))
    movie = Movie.find_by_id(movie_id)
    if movie:
        print(f"{movie[1]} ({movie[2]})")
    else:
        print("Movie not found.")

def delete_movie():
    movie_id = int(input("Enter movie ID to delete: "))
    movie = Movie.find_by_id(movie_id)
    if movie:
        Movie.delete(movie_id)
        print("Movie deleted successfully.")
    else:
        print("Movie not found.")

def actor_menu():
    while True:
        print("\nActor Menu:")
        print("1. Add Actor")
        print("2. View All Actors")
        print("3. Find Actor by ID")
        print("4. Delete Actor")
        print("5. Go Back")

        choice = input("Choose an option: ")
        if choice == "1":
            add_actor()
        elif choice == "2":
            display_actors()
        elif choice == "3":
            find_actor_by_id()
        elif choice == "4":
            delete_actor()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def add_actor():
    name = input("Enter actor name: ")
    try:
        age = int(input("Enter actor age: "))
        actor = Actor(name, age)
        actor.save()
        print(f"Actor '{name}' added successfully.")
    except ValueError as e:
        print(e)

def display_actors():
    actors = Actor.get_all()
    for actor in actors:
        print(f"{actor[1]}, Age: {actor[2]}")

def find_actor_by_id():
    actor_id = int(input("Enter actor ID: "))
    actor = Actor.find_by_id(actor_id)
    if actor:
        print(f"{actor[1]}, Age: {actor[2]}")
    else:
        print("Actor not found.")

def delete_actor():
    actor_id = int(input("Enter actor ID to delete: "))
    actor = Actor.find_by_id(actor_id)
    if actor:
        Actor.delete(actor_id)
        print("Actor deleted successfully.")
    else:
        print("Actor not found.")
