import sqlite3
class Actor:
    TABLE_NAME = 'actors'

    def __init__(self, name, age, movie_id, id=None):
        self._id = id
        self._name = name
        self._age = age
        self._movie_id = movie_id

    @property
    def id(self):
        return self._id

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
        if value < 0:
            raise ValueError("Age cannot be negative.")
        self._age = value

    @property
    def movie_id(self):
        return self._movie_id

    @movie_id.setter
    def movie_id(self, value):
        self._movie_id = value

    @classmethod
    def create(cls, name, age, movie_id):
        actor = cls(name, age, movie_id)
        conn = sqlite3.connect('movies_actors.db')
        with conn:
            cursor = conn.execute(f'INSERT INTO {cls.TABLE_NAME} (name, age, movie_id) VALUES (?, ?, ?)', (actor.name, actor.age, actor.movie_id))
            actor._id = cursor.lastrowid  # Set the ID of the actor from the last insert
        conn.close()
        return actor  # Return the newly created actor object

    @classmethod
    def get_all(cls):
        conn = sqlite3.connect('movies_actors.db')
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM {cls.TABLE_NAME}')
        actors = cursor.fetchall()
        conn.close()
        return [cls(name=row[1], age=row[2], movie_id=row[3], id=row[0]) for row in actors]  # Include id in the returned object

    @classmethod
    def delete(cls, actor_id):
        conn = sqlite3.connect('movies_actors.db')
        with conn:
            conn.execute(f'DELETE FROM {cls.TABLE_NAME} WHERE id = ?', (actor_id,))
        conn.close()

    @classmethod
    def find_by_id(cls, actor_id):
        conn = sqlite3.connect('movies_actors.db')
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM {cls.TABLE_NAME} WHERE id = ?', (actor_id,))
        row = cursor.fetchone()
        conn.close()
        return cls(name=row[1], age=row[2], movie_id=row[3], id=row[0]) if row else None
