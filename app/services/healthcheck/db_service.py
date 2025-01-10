from .idatabase import IDatabaseHealthCheck


class DBServiceHealthCheck(IDatabaseHealthCheck):
    def __init__(self, db_repository: IDatabaseHealthCheck):
        self.db_repository = db_repository

    def is_up(self):
        return self.db_repository.is_up()
