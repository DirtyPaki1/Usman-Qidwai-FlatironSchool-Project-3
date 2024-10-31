def validate_age(value):
    if value < 0:
        raise ValueError("Age cannot be negative.")
    return value

def validate_year(value):
    if value < 1888:  # The first movie was made in 1888
        raise ValueError("Year cannot be before 1888.")
    return value
