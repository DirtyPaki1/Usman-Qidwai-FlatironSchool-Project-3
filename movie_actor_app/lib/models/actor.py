from lib.database import get_connection
from lib.helpers import validate_age

class Actor:
    def __init__(self, name, age, movie_title=None):
        self.name = name
        self.age = age
        self.movie_title = movie_title

    @classmethod
    def create_table(cls):
        with get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS actors (
                    name TEXT PRIMARY KEY,
                    age INTEGER NOT NULL,
                    movie_title TEXT,
                    FOREIGN KEY(movie_title) REFERENCES movies(title) ON DELETE SET NULL
                )
            """)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = validate_age(value)

    def save(self):
        with get_connection() as conn:
            conn.execute("INSERT OR REPLACE INTO actors (name, age, movie_title) VALUES (?, ?, ?)", (self.name, self.age, self.movie_title))

    def delete(self):
        with get_connection() as conn:
            conn.execute("DELETE FROM actors WHERE name = ?", (self.name,))

    @classmethod
    def get_all(cls):
        with get_connection() as conn:
            return [cls(name=row[0], age=row[1], movie_title=row[2]) for row in conn.execute("SELECT name, age, movie_title FROM actors")]

    @classmethod
    def find_by_name(cls, name):
        with get_connection() as conn:
            row = conn.execute("SELECT name, age, movie_title FROM actors WHERE name = ?", (name,)).fetchone()
            return cls(name=row[0], age=row[1], movie_title=row[2]) if row else None

    @classmethod
    def find_by_movie_title(cls, movie_title):
        with get_connection() as conn:
            return [cls(name=row[0], age=row[1], movie_title=row[2]) for row in conn.execute("SELECT name, age, movie_title FROM actors WHERE movie_title = ?", (movie_title,))]

    def form(self):
        return f"Actor: {self.name}, Age: {self.age}, Movie Title: {self.movie_title}"
