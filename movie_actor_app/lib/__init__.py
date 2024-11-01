import sqlite3

def initialize_tables():
    conn = sqlite3.connect('movies_actors.db')
    cursor = conn.cursor()

    # Create Movie table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        year INTEGER NOT NULL
    )
    ''')

    # Create Actor table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS actors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        movie_id INTEGER,
        FOREIGN KEY (movie_id) REFERENCES movies (id) ON DELETE CASCADE
    )
    ''')

    conn.commit()
    conn.close()
