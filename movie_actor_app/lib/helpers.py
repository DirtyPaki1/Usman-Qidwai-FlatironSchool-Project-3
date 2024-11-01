def display_menu(options):
    print("\n".join(f"{i + 1}. {option}" for i, option in enumerate(options)))

def validate_integer_input(prompt, min_value=None):
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}. Please try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
