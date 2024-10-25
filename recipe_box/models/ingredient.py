# models/ingredient.py
class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @classmethod
    def create(cls, name, quantity, unit):
        return cls(name, quantity, unit)

    @staticmethod
    def get_all():
        # Implement logic to fetch all ingredients from database
        # For now, let's return a dummy list
        return [
            Ingredient("Flour", 250, "g"),
            Ingredient("Eggs", 3, "whole"),
            Ingredient("Milk", 200, "ml")
        ]

    @staticmethod
    def find_by_name(name):
        # Implement logic to find ingredient by name from database
        # For now, let's return None
        return None

    def delete(self):
        # Implement logic to delete ingredient from database
        pass
