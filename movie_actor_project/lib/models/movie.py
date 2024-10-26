from lib.helpers import connect_db, validate_nonempty_string, validate_positive_integer

class Movie:
    def __init__(self, title, release_year):
        self.title = title
        self.release_year = release_year

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        validate_nonempty_string(value, "Title")
        self._title = value

    @property
    def release_year(self):
        return self._release_year

    @release_year.setter
    def release_year(self, value):
        validate_positive_integer(value, "Release Year")
        self._release_year = value

    @classmethod
    def create(cls, title, release_year):
        """Creates a new movie record in the database."""
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO movies (title, release_year) VALUES (?, ?)", (title, release_year))
            conn.commit()

    @classmethod
    def delete(cls, movie_id):
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
            conn.commit()

    @classmethod
    def get_all(cls):
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM movies")
            return cursor.fetchall()

    @classmethod
    def find_by_id(cls, movie_id):
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM movies WHERE id = ?", (movie_id,))
            return cursor.fetchone()
