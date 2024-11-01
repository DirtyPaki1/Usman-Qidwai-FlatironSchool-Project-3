def display_menu(options):
    print("\n" + "\n".join([f"{i + 1}. {option}" for i, option in enumerate(options)]) + "\n")

def validate_integer_input(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                raise ValueError(f"Value must be between {min_value} and {max_value}.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}")
