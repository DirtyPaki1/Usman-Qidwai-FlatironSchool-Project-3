import sqlite3

class Actor:
    def __init__(self, name, age, movie_id=None):
        self.name = name
        self.age = age
        self.movie_id = movie_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and value.strip():
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string.")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, int) and value > 0:
            self._age = value
        else:
            raise ValueError("Age must be a positive integer.")

    @classmethod
    def create_table(cls):
        with sqlite3.connect("lib/movie_actor.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS actors (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    movie_id INTEGER,
                    FOREIGN KEY (movie_id) REFERENCES movies(id) ON DELETE SET NULL
                )
            """)
            conn.commit()

    def save(self):
        with sqlite3.connect("lib/movie_actor.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO actors (name, age, movie_id) VALUES (?, ?, ?)",
                           (self.name, self.age, self.movie_id))
            conn.commit()

    @classmethod
    def get_all(cls):
        with sqlite3.connect("lib/movie_actor.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM actors")
            return cursor.fetchall()

    @classmethod
    def find_by_id(cls, actor_id):
        with sqlite3.connect("lib/movie_actor.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM actors WHERE id = ?", (actor_id,))
            return cursor.fetchone()

    def delete(self):
        with sqlite3.connect("lib/movie_actor.db") as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM actors WHERE name = ?", (self.name,))
            conn.commit()
