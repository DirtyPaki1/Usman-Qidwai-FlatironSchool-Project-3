# lib/database.py
import sqlite3

DATABASE_NAME = 'lib/movie_actor.db'

def get_connection():
    return sqlite3.connect(DATABASE_NAME)

def create_tables():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL UNIQUE,
                release_year INTEGER NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS actors (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                movie_id INTEGER,
                FOREIGN KEY (movie_id) REFERENCES movies(id) ON DELETE SET NULL
            )
        """)
        conn.commit()
