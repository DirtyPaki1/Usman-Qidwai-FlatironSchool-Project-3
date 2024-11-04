def validate_integer_input(prompt):
    """Get integer input from user, with validation."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def validate_string_input(prompt):
    """Get string input from user, with validation."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")

def display_objects(objects, title):
    """Display a list of objects in a user-friendly way."""
    if objects:
        print(f"\n{title}:")
        for i, obj in enumerate(objects, start=1):
            print(f"{i}. {obj}")
    else:
        print("No objects found.")
