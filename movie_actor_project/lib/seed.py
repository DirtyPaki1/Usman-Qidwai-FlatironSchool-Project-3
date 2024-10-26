import sqlite3
import os

# Path to the database file
DB_PATH = "lib/movie_actor.db"

def create_tables():
    """Create tables for movies and actors."""
    print(f"Using database: {os.path.abspath(DB_PATH)}")  # Print the absolute path
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        
        # Create movies table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                release_year INTEGER NOT NULL
            )
        """)
        
        # Create actors table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS actors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                movie_id INTEGER,
                FOREIGN KEY (movie_id) REFERENCES movies(id) ON DELETE CASCADE
            )
        """)

        conn.commit()
        print("Tables created successfully.")

if __name__ == "__main__":
    create_tables()
