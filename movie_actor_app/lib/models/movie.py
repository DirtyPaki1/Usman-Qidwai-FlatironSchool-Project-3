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

    @property
    def year(self):
        return self._year

    @classmethod
    def create(cls, title, year):
        """Create a new movie in the database."""
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO movies (title, year) VALUES (?, ?)", (title, year))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        """Retrieve all movies."""
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM movies")
        movies = cursor.fetchall()
        conn.close()
        return [cls(title=row[1], year=row[2], id=row[0]) for row in movies]

    @classmethod
    def find_by_title(cls, title):
        """Find a movie by title."""
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM movies WHERE title = ?", (title,))
        result = cursor.fetchone()
        conn.close()
        if result:
            return cls(title=result[1], year=result[2], id=result[0])
        return None

    @classmethod
    def delete(cls, title):
        """Delete a movie and its associated actors by title."""
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM actors WHERE movie_id = (SELECT id FROM movies WHERE title = ?)", (title,))
        cursor.execute("DELETE FROM movies WHERE title = ?", (title,))
        conn.commit()
        conn.close()

     
    



    def get_associated_actors(self):
        """Retrieve all actors associated with this movie."""
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM actors WHERE movie_id = (SELECT id FROM movies WHERE title = ?)", (self.title,))
        actors = cursor.fetchall()
        conn.close()
        return [actors(id=row[0], name=row[1], age=row[2], movie_id=row[3]) for row in actors]

    


    def __str__(self):
        return f"{self.title} ({self.year})"
 

