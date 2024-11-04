import sqlite3
from lib.database import DATABASE_NAME

class Movie:
    def __init__(self, title, year, id=None):
        self._id = id  # Internal ID for ORM use
        self._title = title
        self._year = year

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
        if not isinstance(value, int) or value < 1888:  # The year of the first movie
            raise ValueError("Year must be a valid year after 1887.")
        self._year = value

    @property
    def id(self):
        return self._id  # Exposing the ID property if needed

    @classmethod
    def create(cls, title, year):
        """Create a new movie in the database."""
        movie_instance = cls(title, year)
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO movies (title, year) VALUES (?, ?)", (movie_instance.title, movie_instance.year))
            conn.commit()

    @classmethod
    def get_all(cls):
        """Retrieve all movies."""
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM movies")
            movies = cursor.fetchall()
        return [cls(title=row[1], year=row[2], id=row[0]) for row in movies]

    @classmethod
    def find_by_title(cls, title):
        """Find a movie by title."""
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM movies WHERE title = ?", (title,))
            result = cursor.fetchone()
        if result:
            return cls(title=result[1], year=result[2], id=result[0])
        return None

    @classmethod
    def delete(cls, title):
        """Delete a movie and its associated actors by title."""
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM actors WHERE movie_id = (SELECT id FROM movies WHERE title = ?)", (title,))
            cursor.execute("DELETE FROM movies WHERE title = ?", (title,))
            conn.commit()

    def get_associated_actors(self):
        """Retrieve all actors associated with this movie."""
        from lib.models.actor import Actor  # Local import to avoid circular import

        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM actors WHERE movie_id = ?", (self.id,))
            actors = cursor.fetchall()
        return [Actor(id=row[0], name=row[1], age=row[2], movie_id=self.id) for row in actors]

    def __str__(self):
        return f"{self.title} ({self.year})"
