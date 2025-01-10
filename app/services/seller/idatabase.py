from abc import ABCMeta, abstractmethod


class IDatabaseSeller(metaclass=ABCMeta):
    @abstractmethod
    def get_sellers(self):
        raise NotImplementedError

    @abstractmethod
    def get_seller_by_id(self, id: int):
        raise NotImplementedError

    @abstractmethod
    def get_seller_by_phone(self, phone: str):
        raise NotImplementedError

    @abstractmethod
    def create_seller(self, seller):
        raise NotImplementedError

    @abstractmethod
    def update_seller(self, id: int, seller):
        raise NotImplementedError

    @abstractmethod
    def delete_seller(self, id: int):
        raise NotImplementedError
