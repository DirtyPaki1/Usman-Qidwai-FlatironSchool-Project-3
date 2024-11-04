import sqlite3
from lib.database import DATABASE_NAME

class Actor:
    def __init__(self, name, age, movie_id=None, id=None):
        self._id = id  # Internal ID for ORM use
        self._name = name
        self._age = age
        self._movie_id = movie_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty.")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0:  # Age cannot be negative
            raise ValueError("Age must be a non-negative integer.")
        self._age = value

    @property
    def movie_id(self):
        return self._movie_id

    @movie_id.setter
    def movie_id(self, value):
        self._movie_id = value  # Optional setter for movie_id, if needed

    @classmethod
    def create(cls, name, age, movie_title):
        """Create a new actor in the database."""
        from lib.models.movie import Movie  # Local import to avoid circular import
        
        movie = Movie.find_by_title(movie_title)  # Reference to the Movie class
        if not movie:
            raise ValueError("Cannot add an actor to a movie that does not exist.")
        
        actor_instance = cls(name, age, movie.id)
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO actors (name, age, movie_id) VALUES (?, ?, ?)", (actor_instance.name, actor_instance.age, actor_instance.movie_id))
            conn.commit()

    @classmethod
    def delete(cls, name):
        """Delete an actor by name."""
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM actors WHERE name = ?", (name,))
            conn.commit()

    @classmethod
    def get_all(cls):
        """Retrieve all actors."""
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM actors")
            actors = cursor.fetchall()
        return [cls(id=row[0], name=row[1], age=row[2], movie_id=row[3]) for row in actors]

    def __str__(self):
        return f"{self.name}, Age: {self.age}"
