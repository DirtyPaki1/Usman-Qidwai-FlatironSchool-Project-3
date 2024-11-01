import sqlite3

class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    @classmethod
    def create(cls, title, year):
        conn = sqlite3.connect('movies_actors.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO movies (title, year) VALUES (?, ?)", (title, year))
        conn.commit()
        conn.close()

    @classmethod
    def delete(cls, movie_id):
        conn = sqlite3.connect('movies_actors.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM movies WHERE id=?", (movie_id,))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = sqlite3.connect('movies_actors.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, year FROM movies")
        movies = [cls(row[1], row[2]) for row in cursor.fetchall()]
        conn.close()
        return movies

    @classmethod
    def find_by_id(cls, movie_id):
        conn = sqlite3.connect('movies_actors.db')
        cursor = conn.cursor()
        cursor.execute("SELECT title, year FROM movies WHERE id=?", (movie_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(row[0], row[1])
        return None

    @classmethod
    def find_by_title(cls, title):
        conn = sqlite3.connect('movies_actors.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, year FROM movies WHERE title=?", (title,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(row[0], row[1])
        return None
