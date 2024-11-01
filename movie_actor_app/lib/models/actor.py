import sqlite3

class Actor:
    def __init__(self, name, age, movie_id):
        self.name = name
        self.age = age
        self.movie_id = movie_id

    @classmethod
    def create(cls, name, age, movie_id):
        conn = sqlite3.connect('movies_actors.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO actors (name, age, movie_id) VALUES (?, ?, ?)", (name, age, movie_id))
        conn.commit()
        conn.close()

    @classmethod
    def delete(cls, actor_id):
        conn = sqlite3.connect('movies_actors.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM actors WHERE id=?", (actor_id,))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = sqlite3.connect('movies_actors.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, age, movie_id FROM actors")
        actors = [cls(row[1], row[2], row[3]) for row in cursor.fetchall()]
        conn.close()
        return actors

    @classmethod
    def find_by_id(cls, actor_id):
        conn = sqlite3.connect('movies_actors.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name, age, movie_id FROM actors WHERE id=?", (actor_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(row[0], row[1], row[2])
        return None

    @classmethod
    def delete_by_movie_id(cls, movie_id):
        conn = sqlite3.connect('movies_actors.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM actors WHERE movie_id=?", (movie_id,))
        conn.commit()
        conn.close()

    @classmethod
    def get_by_movie_id(cls, movie_id):
        conn = sqlite3.connect('movies_actors.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, age FROM actors WHERE movie_id=?", (movie_id,))
        actors = [cls(row[1], row[2], movie_id) for row in cursor.fetchall()]
        conn.close()
        return actors
