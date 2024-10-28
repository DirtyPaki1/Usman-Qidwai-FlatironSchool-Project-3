import sqlite3
from lib.helpers import validate_year

class Movie:
    def __init__(self, title, release_year):
        self.title = title
        self.release_year = release_year

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and value.strip():
            self._title = value
        else:
            raise ValueError("Title must be a non-empty string.")

    @property
    def release_year(self):
        return self._release_year

    @release_year.setter
    def release_year(self, value):
        self._release_year = validate_year(value)

    @classmethod
    def create_table(cls):
        with sqlite3.connect("lib/movie_actor.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS movies (
                    id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL UNIQUE,
                    release_year INTEGER NOT NULL
                )
            """)
            conn.commit()
    def save(self):
        with sqlite3.connect("lib/movie_actor.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO movies (title, release_year) VALUES (?, ?)",
                           (self.title, self.release_year))
            conn.commit()

    @classmethod
    def get_all(cls):
        with sqlite3.connect("lib/movie_actor.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM movies")
            return cursor.fetchall()

    @classmethod
    def find_by_id(cls, movie_id):
        with sqlite3.connect("lib/movie_actor.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM movies WHERE id = ?", (movie_id,))
            return cursor.fetchone()

    def delete(self):
        with sqlite3.connect("lib/movie_actor.db") as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM movies WHERE title = ?", (self.title,))
            conn.commit()

    def get_actors(self):
        with sqlite3.connect("lib/movie_actor.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM actors WHERE movie_id = ?", (self.id,))
            return cursor.fetchall()
