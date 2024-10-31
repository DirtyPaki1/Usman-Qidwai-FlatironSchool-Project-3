def format_actor(actor):
    return f"Actor: {actor.name}, Age: {actor.age}"

def format_movie(movie):
    return f"Movie: {movie.title}, Year: {movie.year}"

def validate_year(year):
    if not isinstance(year, int) or year < 1888 or year > 2025:
        raise ValueError("Year must be an integer between 1888 and 2025.")
    return year
