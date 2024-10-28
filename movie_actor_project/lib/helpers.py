def validate_year(year):
    if isinstance(year, int) and 1800 <= year <= 2100:
        return year
    else:
        raise ValueError("Invalid year. Please enter a year between 1800 and 2100.")

def validate_age(age):
    if isinstance(age, int) and age > 0:
        return age
    else:
        raise ValueError("Invalid age. Age must be a positive integer.")
