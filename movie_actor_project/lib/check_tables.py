import sqlite3

def check_tables():
    # Connect to the SQLite database
    with sqlite3.connect("lib/movie_actor.db") as conn:
        cursor = conn.cursor()
        # Execute a query to get all table names
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
    return tables

if __name__ == "__main__":
    tables = check_tables()
    print("Tables in the database:")
    if tables:
        for table in tables:
            print(f"- {table[0]}")
    else:
        print("No tables found.")
