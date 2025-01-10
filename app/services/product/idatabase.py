from abc import ABCMeta, abstractmethod


class IDatabaseProduct(metaclass=ABCMeta):
    @abstractmethod
    def get_products(self):
        raise NotImplementedError

    @abstractmethod
    def get_product_by_id(self, id: int):
        raise NotImplementedError

    @abstractmethod
    def get_product_by_sku(self, sku: str):
        raise NotImplementedError

    @abstractmethod
    def create_product(self, product):
        raise NotImplementedError

    @abstractmethod
    def update_product(self, id: int, product):
        raise NotImplementedError

    @abstractmethod
    def delete_product(self, id: int):
        raise NotImplementedError
