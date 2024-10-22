class Ingredient:
    all_ingredients = []

    def __init__(self, name, quantity, unit):
        self.id = len(Ingredient.all_ingredients) + 1
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.recipes = []
        Ingredient.all_ingredients.append(self)

    @classmethod
    def all_ingredients(cls):
        return cls.all_ingredients

    def add_to_recipe(self, recipe):
        self.recipes.append(recipe)
        recipe.add_ingredient(self)

    def remove_from_recipe(self, recipe):
        self.recipes.remove(recipe)
        recipe.remove_ingredient(self)
