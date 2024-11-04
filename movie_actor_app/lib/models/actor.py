import sqlite3
from lib.database import DATABASE_NAME
from lib.models.movie import Movie  # Import the Movie class

class Actor:
    def __init__(self, name, age, movie_id=None, id=None):
        self._id = id  # Internal ID for ORM use
        self._name = name
        self._age = age
        self._movie_id = movie_id

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @classmethod
    def create(cls, name, age, movie_title):
        """Create a new actor in the database."""
        movie = Movie.find_by_title(movie_title)  # Reference to the Movie class
        if not movie:
            raise ValueError("Cannot add an actor to a movie that does not exist.")
        
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO actors (name, age, movie_id) VALUES (?, ?, ?)", (name, age, movie._id))
        conn.commit()
        conn.close()

    @classmethod
    def delete(cls, name):
        """Delete an actor by name."""
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM actors WHERE name = ?", (name,))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        """Retrieve all actors."""
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM actors")
        actors = cursor.fetchall()
        conn.close()
        return [cls(id=row[0], name=row[1], age=row[2], movie_id=row[3]) for row in actors]

    def __str__(self):
        return f"{self.name}, Age: {self.age}"
