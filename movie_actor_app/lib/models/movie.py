import sqlite3

class Movie:
    TABLE_NAME = 'movies'

    def __init__(self, title, year, id=None):
        self.id = id
        self.title = title
        self.year = year

    @property
    def id(self):
        return self._id

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
        if value < 1888:
            raise ValueError("Year must be 1888 or later.")
        self._year = value

    @classmethod
    def create(cls, title, year):
        movie = cls(title, year)
        conn = sqlite3.connect('movies_actors.db')
        with conn:
            cursor = conn.execute(f'INSERT INTO {cls.TABLE_NAME} (title, year) VALUES (?, ?)', (movie.title, movie.year))
            movie._id = cursor.lastrowid
        conn.close()
        return movie

    @classmethod
    def get_all(cls):
        conn = sqlite3.connect('movies_actors.db')
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM {cls.TABLE_NAME}')
        movies = cursor.fetchall()
        conn.close()
        return [cls(title=row[1], year=row[2], id=row[0]) for row in movies]

    @classmethod
    def delete(cls, movie_id):
        conn = sqlite3.connect('movies_actors.db')
        with conn:
            conn.execute(f'DELETE FROM {cls.TABLE_NAME} WHERE id = ?', (movie_id,))
        conn.close()

    @classmethod
    def find_by_title(cls, title):
        conn = sqlite3.connect('movies_actors.db')
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM {cls.TABLE_NAME} WHERE title = ?', (title,))
        row = cursor.fetchone()
        conn.close()
        return cls(title=row[1], year=row[2], id=row[0]) if row else None

    @classmethod
    def find_by_id(cls, movie_id):
        conn = sqlite3.connect('movies_actors.db')
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM {cls.TABLE_NAME} WHERE id = ?', (movie_id,))
        row = cursor.fetchone()
        conn.close()
        return cls(title=row[1], year=row[2], id=row[0]) if row else None

    def get_actors(self):
        # Dynamically import Actor here to avoid circular import
        from lib.models.actor import Actor
        conn = sqlite3.connect('movies_actors.db')
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM {Actor.TABLE_NAME} WHERE movie_id = ?', (self.id,))
        actors = cursor.fetchall()
        conn.close()
        return [Actor(name=row[1], age=row[2], movie_id=row[3], id=row[0]) for row in actors]
