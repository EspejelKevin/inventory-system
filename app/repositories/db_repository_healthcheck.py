from pymysql import Connection
from pymysql.cursors import Cursor
from services import IDatabaseHealthCheck


class DBRepositoryHealthCheck(IDatabaseHealthCheck):
    def __init__(self, db_session) -> None:
        self.db_session = db_session

    def is_up(self):
        with self.db_session() as session:
            return session.is_up()
