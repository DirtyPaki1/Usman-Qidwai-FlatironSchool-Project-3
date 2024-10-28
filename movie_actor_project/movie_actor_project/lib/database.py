import sqlite3

DATABASE_NAME = 'lib/movie_actor.db'

def get_connection():
    return sqlite3.connect(DATABASE_NAME)

def create_tables():
    from lib.models.movie import Movie
    from lib.models.actor import Actor
    Movie.create_table()
    Actor.create_table()
