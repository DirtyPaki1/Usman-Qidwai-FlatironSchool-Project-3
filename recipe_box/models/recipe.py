class Recipe:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.ingredients = []

    @classmethod
    def create(cls, title, description, category):
        return cls(title, description, category)

    @staticmethod
    def get_all():
        return [
            Recipe("Spaghetti Bolognese", "Classic Italian pasta dish", "Main Course"),
            Recipe("Chicken Tikka Masala", "Popular Indian-inspired British dish", "Main Course"),
            Recipe("Chocolate Cake", "Moist chocolate cake recipe", "Dessert")
        ]

    @staticmethod
    def find_by_id(id):
        return None  # Placeholder implementation

    def delete(self):
        pass  # Placeholder implementation
