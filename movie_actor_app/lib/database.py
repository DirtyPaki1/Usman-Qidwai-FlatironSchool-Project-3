import sqlite3

def get_connection():
    return sqlite3.connect('movie_actor.db')

def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            year INTEGER NOT NULL
        )
    ''')
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
