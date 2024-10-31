from lib.database import get_connection
from lib.helpers import validate_year
from lib.models.actor import Actor


class Movie:
    def __init__(self, title, year, id=None):
        self.id = id
        self.title = title
        self.year = year

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Title cannot be empty.")
        self._title = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = validate_year(value)

    def save(self):
        with get_connection() as conn:
            if self.id is None:
                conn.execute("INSERT INTO movies (title, year) VALUES (?, ?)", (self.title, self.year))
                self.id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
            else:
                conn.execute("UPDATE movies SET title = ?, year = ? WHERE id = ?", (self.title, self.year, self.id))

    def delete(self):
        with get_connection() as conn:
            conn.execute("DELETE FROM movies WHERE id = ?", (self.id,))

    @classmethod
    def get_all(cls):
        with get_connection() as conn:
            return [cls(id=row[0], title=row[1], year=row[2]) for row in conn.execute("SELECT id, title, year FROM movies")]

    @classmethod
    def find_by_title(cls, title):
        with get_connection() as conn:
            row = conn.execute("SELECT id, title, year FROM movies WHERE title = ?", (title,)).fetchone()
            return cls(id=row[0], title=row[1], year=row[2]) if row else None

    def get_actors(self):
        return Actor.find_by_movie_title(self.title)

    def format_movie(self):
        return f"Movie: {self.title}, Year: {self.year}"
