from services import IDatabaseHealthCheck


class ReadinessController:
    def __init__(self, db_service: IDatabaseHealthCheck) -> None:
        self.db_service = db_service

    def execute(self):
        return self.db_service.is_up()
