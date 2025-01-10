from abc import ABCMeta, abstractmethod


class IDatabaseClient(metaclass=ABCMeta):
    @abstractmethod
    def get_clients(self):
        raise NotImplementedError

    @abstractmethod
    def get_client_by_id(self, id: int):
        raise NotImplementedError

    @abstractmethod
    def get_client_by_email(self, email: str):
        raise NotImplementedError

    @abstractmethod
    def get_client_by_phone(self, phone: str):
        raise NotImplementedError

    @abstractmethod
    def create_client(self, client):
        raise NotImplementedError

    @abstractmethod
    def update_client(self, id: int, client):
        raise NotImplementedError

    @abstractmethod
    def delete_client(self, id: int):
        raise NotImplementedError
