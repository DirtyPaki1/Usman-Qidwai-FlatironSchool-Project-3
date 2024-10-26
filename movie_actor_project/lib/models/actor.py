from lib.helpers import connect_db, validate_nonempty_string, validate_positive_integer

class Actor:
    def __init__(self, name, age, movie_id):
        self.name = name
        self.age = age
        self.movie_id = movie_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        validate_nonempty_string(value, "Name")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        validate_positive_integer(value, "Age")
        self._age = value

    @property
    def movie_id(self):
        return self._movie_id

    @movie_id.setter
    def movie_id(self, value):
        validate_positive_integer(value, "Movie ID")
        self._movie_id = value

    @classmethod
    def create(cls, name, age, movie_id):
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO actors (name, age, movie_id) VALUES (?, ?, ?)", (name, age, movie_id))
            conn.commit()

    @classmethod
    def delete(cls, actor_id):
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM actors WHERE id = ?", (actor_id,))
            conn.commit()

    @classmethod
    def get_all(cls):
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM actors")
            return cursor.fetchall()

    @classmethod
    def find_by_id(cls, actor_id):
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM actors WHERE id = ?", (actor_id,))
            return cursor.fetchone()
