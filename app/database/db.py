from contextlib import contextmanager
from typing import Iterator

from pymysql import connect


class Connection:
    def __init__(self, host: str, user: str, password: str, db: str) -> None:
        self._connection = connect(
            host=host, user=user, password=password, database=db, autocommit=True)

    def __enter__(self) -> 'Connection':
        return self

    def is_up(self) -> dict:
        data = {'message': 'Connection established with MySQL'}

        try:
            with self._connection.cursor() as cursor:
                query = 'SELECT 1'
                cursor.execute(query)
        except Exception:
            data['message'] = 'Connection refused with MySQL'

        return data

    def get_client(self):
        return self._connection

    def __exit__(self, *exc) -> None:
        self._connection.close()


class Database:
    def __init__(self, host: str, user: str, password: str, db: str) -> None:
        self._connection = Connection(host, user, password, db)

    @contextmanager
    def session(self) -> Iterator[Connection]:
        yield self._connection
