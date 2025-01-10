from abc import ABCMeta, abstractmethod


class IDatabaseInventory(metaclass=ABCMeta):
    @abstractmethod
    def get_inventories(self):
        raise NotImplementedError

    @abstractmethod
    def get_inventory_by_id(self, id: int):
        raise NotImplementedError

    @abstractmethod
    def get_inventory_by_code(self, code: str):
        raise NotImplementedError

    @abstractmethod
    def create_inventory(self, inventory):
        raise NotImplementedError

    @abstractmethod
    def update_inventory(self, id: int, inventory):
        raise NotImplementedError

    @abstractmethod
    def delete_inventory(self, id: int):
        raise NotImplementedError
