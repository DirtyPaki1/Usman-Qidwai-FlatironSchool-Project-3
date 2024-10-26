import sqlite3

DB_PATH = "lib/movie_actor.db"

def connect_db():
    """Creates a connection to the SQLite database."""
    return sqlite3.connect(DB_PATH)

def validate_nonempty_string(value, field_name):
    """Validates that a string is nonempty."""
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} must be a non-empty string.")

def validate_positive_integer(value, field_name):
    """Validates that a value is a positive integer."""
    if not isinstance(value, int) or value <= 0:
        raise ValueError(f"{field_name} must be a positive integer.")
