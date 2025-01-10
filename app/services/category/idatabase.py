from abc import ABCMeta, abstractmethod


class IDatabaseCategory(metaclass=ABCMeta):
    @abstractmethod
    def get_categories(self):
        raise NotImplementedError

    @abstractmethod
    def get_category_by_id(self, id: int):
        raise NotImplementedError

    @abstractmethod
    def get_category_by_name(self, name: str):
        raise NotImplementedError

    @abstractmethod
    def create_category(self, category):
        raise NotImplementedError

    @abstractmethod
    def update_category(self, id: int, category):
        raise NotImplementedError

    @abstractmethod
    def delete_category(self, id: int):
        raise NotImplementedError
