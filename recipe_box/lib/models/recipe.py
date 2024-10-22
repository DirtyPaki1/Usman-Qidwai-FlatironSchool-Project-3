class Recipe:
    all_recipes = []
    next_id = 1

    def __init__(self, title, description, cuisine, difficulty, cooking_time):
        self.id = Recipe.next_id
        Recipe.next_id += 1
        self.title = title
        self.description = description
        self.cuisine = cuisine
        self.difficulty = difficulty
        self.cooking_time = cooking_time
        self.ingredients = []
        self.steps = []
        self.tags = []
        Recipe.all_recipes.append(self)

    @classmethod
    def all_recipes(cls):
        return cls.all_recipes

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def add_step(self, step):
        self.steps.append(step)

    def add_tag(self, tag):
        self.tags.append(tag)

    def remove_ingredient(self, ingredient):
        self.ingredients.remove(ingredient)

    def remove_step(self, index):
        if 0 <= index < len(self.steps):
            del self.steps[index]
        else:
            raise ValueError("Step index out of range")

    def remove_tag(self, tag):
        self.tags.remove(tag)
