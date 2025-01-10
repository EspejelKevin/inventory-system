from .idatabase import IDatabaseCategory


class DBServiceCategory(IDatabaseCategory):
    def __init__(self, db_repository: IDatabaseCategory):
        self.db_repository = db_repository

    def get_categories(self):
        return self.db_repository.get_categories()

    def get_category_by_id(self, id: int):
        return self.db_repository.get_category_by_id(id)

    def get_category_by_name(self, name: str):
        return self.db_repository.get_category_by_name(name)

    def create_category(self, category):
        return self.db_repository.create_category(category)

    def update_category(self, id: int, category):
        return self.db_repository.update_category(id, category)

    def delete_category(self, id: int):
        return self.db_repository.delete_category(id)
