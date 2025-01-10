from .idatabase import IDatabaseClient


class DBServiceClient(IDatabaseClient):
    def __init__(self, db_repository: IDatabaseClient) -> None:
        self.db_repository = db_repository

    def get_clients(self):
        return self.db_repository.get_clients()

    def get_client_by_id(self, id):
        return self.db_repository.get_client_by_id(id)

    def get_client_by_email(self, email):
        return self.db_repository.get_client_by_email(email)

    def get_client_by_phone(self, phone):
        return self.db_repository.get_client_by_phone(phone)

    def create_client(self, client):
        return self.db_repository.create_client(client)

    def update_client(self, id, client):
        return self.db_repository.update_client(id, client)

    def delete_client(self, id):
        return self.db_repository.delete_client(id)
