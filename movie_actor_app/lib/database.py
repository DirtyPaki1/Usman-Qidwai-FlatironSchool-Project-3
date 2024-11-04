import sqlite3

DATABASE_NAME = "movies_actors.db"

def initialize_database():
    """Initialize the database and create tables."""
    conn = sqlite3.connect(DATABASE_NAME)
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                year INTEGER NOT NULL
            )
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS actors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                movie_id INTEGER,
                FOREIGN KEY (movie_id) REFERENCES movies (id) ON DELETE CASCADE
            )
        ''')
    conn.close()
