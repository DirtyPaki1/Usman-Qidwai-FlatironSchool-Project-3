from lib.database import get_connection
from lib.helpers import validate_year

class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    @classmethod
    def create_table(cls):
        with get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS movies (
                    title TEXT PRIMARY KEY,
                    year INTEGER NOT NULL
                )
            """)

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = validate_year(value)

    def save(self):
        with get_connection() as conn:
            conn.execute("INSERT OR REPLACE INTO movies (title, year) VALUES (?, ?)", (self.title, self.year))

    def delete(self):
        with get_connection() as conn:
            conn.execute("DELETE FROM movies WHERE title = ?", (self.title,))

    @classmethod
    def get_all(cls):
        with get_connection() as conn:
            return [cls(title=row[0], year=row[1]) for row in conn.execute("SELECT title, year FROM movies")]

    @classmethod
    def find_by_title(cls, title):
        with get_connection() as conn:
            row = conn.execute("SELECT title, year FROM movies WHERE title = ?", (title,)).fetchone()
            return cls(title=row[0], year=row[1]) if row else None

    def get_actors(self):
        from lib.models.actor import Actor
        return Actor.find_by_movie_title(self.title)

    def form(self):
        return f"Movie: {self.title}, Year: {self.year}"
