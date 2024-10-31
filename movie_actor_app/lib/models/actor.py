from lib.database import get_connection


class Actor:
    def __init__(self, id=None, name=None, age=None, movie_id=None):
        self.id = id
        self._name = name
        self._age = age
        self.movie_id = movie_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Actor name cannot be empty.")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Actor age must be a non-negative integer.")
        self._age = value

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("INSERT INTO actors (name, age, movie_id) VALUES (?, ?, ?)", (self.name, self.age, self.movie_id))
            self.id = cursor.lastrowid
        else:
            cursor.execute("UPDATE actors SET name=?, age=?, movie_id=? WHERE id=?", (self.name, self.age, self.movie_id, self.id))
        conn.commit()
        conn.close()

    @classmethod
    def delete(cls, actor_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM actors WHERE id = ?", (actor_id,))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, age, movie_id FROM actors")
        rows = cursor.fetchall()
        conn.close()
        return [cls(id=row[0], name=row[1], age=row[2], movie_id=row[3]) for row in rows]

    @classmethod
    def find_by_movie_title(cls, movie_title):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, age FROM actors WHERE movie_id = (SELECT id FROM movies WHERE title = ?)", (movie_title,))
        rows = cursor.fetchall()
        conn.close()
        return [cls(id=row[0], name=row[1], age=row[2]) for row in rows]
