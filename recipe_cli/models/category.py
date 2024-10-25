
class Category:
    def __init__(self, id=None, name=""):
        self.id = id
        self.name = name

    @classmethod
    def create(cls, name):
        return cls(name=name)

    @classmethod
    def delete(cls, id):
        # Delete logic here
        pass

    @classmethod
    def get_all(cls):
        # Get all categories logic here
        pass

    @classmethod
    def find_by_id(cls, id):
        # Find category by ID logic here
        pass

    @classmethod
    def find_by_name(cls, name):
        # Find category by name logic here
        pass

    def __repr__(self):
        return f"Category(id={self.id}, name='{self.name}')"

    def save(self):
        # Save category to database logic here
        pass