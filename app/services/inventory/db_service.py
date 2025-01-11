from .idatabase import IDatabaseInventory


class DBServiceInventory(IDatabaseInventory):
    def __init__(self, db_repository: IDatabaseInventory) -> None:
        self.db_repository = db_repository

    def get_inventories(self):
        return self.db_repository.get_inventories()

    def get_inventory_by_id(self, id):
        return self.db_repository.get_inventory_by_id(id)

    def get_inventory_by_code(self, code):
        return self.db_repository.get_inventory_by_code(code)

    def create_inventory(self, inventory):
        return self.db_repository.create_inventory(inventory)

    def update_inventory(self, id, inventory):
        return self.db_repository.update_inventory(id, inventory)

    def delete_inventory(self, id):
        return self.db_repository.delete_inventory(id)
