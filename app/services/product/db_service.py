from .idatabase import IDatabaseProduct


class DBServiceProduct(IDatabaseProduct):
    def __init__(self, db_repository: IDatabaseProduct) -> None:
        self.db_repository = db_repository

    def get_products(self):
        return self.db_repository.get_products()

    def get_product_by_id(self, id):
        return self.db_repository.get_product_by_id(id)

    def get_product_by_name(self, name):
        return self.db_repository.get_product_by_name(name)

    def create_product(self, product):
        return self.db_repository.create_product(product)

    def update_product(self, id, product):
        return self.db_repository.update_product(id, product)

    def delete_product(self, id):
        return self.db_repository.delete_product(id)
