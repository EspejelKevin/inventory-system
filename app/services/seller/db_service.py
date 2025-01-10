from .idatabase import IDatabaseSeller


class DBServiceSeller(IDatabaseSeller):
    def __init__(self, db_repository: IDatabaseSeller) -> None:
        self.db_repository = db_repository

    def get_sellers(self):
        return self.db_repository.get_sellers()

    def get_seller_by_id(self, id):
        return self.db_repository.get_seller_by_id(id)

    def get_seller_by_phone(self, phone):
        return self.db_repository.get_seller_by_phone(phone)

    def create_seller(self, seller):
        return self.db_repository.create_seller(seller)

    def update_seller(self, id, seller):
        return self.db_repository.update_seller(id, seller)

    def delete_seller(self, id):
        return self.db_repository.delete_seller(id)
