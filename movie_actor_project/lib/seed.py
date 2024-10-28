import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.models.movie import Movie
from lib.models.actor import Actor

def initialize_database():
    Movie.create_table()
    Actor.create_table()
    print("Database tables created successfully.")

if __name__ == "__main__":
    initialize_database()
