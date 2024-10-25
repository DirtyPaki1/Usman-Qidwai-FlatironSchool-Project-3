class Recipe:
    def __init__(self, id=None, title="", description="", category_id=None):
        self.id = id
        self.title = title
        self.description = description
        self.category_id = category_id

    @classmethod
    def create(cls, title, description, category_id):
        return cls(title=title, description=description, category_id=category_id)

    @classmethod
    def delete(cls, id):
        # Delete logic here
        pass

    @classmethod
    def get_all(cls):
        # Get all recipes logic here
        pass

    @classmethod
    def find_by_id(cls, id):
        # Find recipe by ID logic here
        pass

    @classmethod
    def find_by_attribute(cls, attribute, value):
        # Find recipe by attribute logic here
        pass

    def __repr__(self):
        return f"Recipe(id={self.id}, title='{self.title}', description='{self.description}', category_id={self.category_id})"

    def save(self):
        # Save recipe to database logic here
        pass