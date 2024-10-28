from lib.models.movie import Movie
from lib.models.actor import Actor
from lib.cli import main_menu

def initialize_database():
    Movie.create_table()  # Ensure movies table is created
    Actor.create_table()  # Ensure actors table is created
    print("Database tables created successfully.")

if __name__ == "__main__":
    initialize_database()  # Call this to create the tables before using them
    main_menu()  # Start the CLI
