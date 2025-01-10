from pymysql import Connection
from pymysql.cursors import Cursor
from schemas import ClientInput
from services import IDatabaseClient


class DBRepositoryClient(IDatabaseClient):
    def __init__(self, db_session) -> None:
        self.db_session = db_session

    def get_clients(self):
        with self.db_session() as session:
            client: Connection = session.get_client()
            cursor: Cursor = client.cursor()
            cursor.execute('SELECT * FROM Client')
            return cursor.fetchall()

    def get_client_by_id(self, id: int):
        with self.db_session() as session:
            client: Connection = session.get_client()
            cursor: Cursor = client.cursor()
            cursor.execute('SELECT * FROM Client WHERE id=%s', (id,))
            return cursor.fetchone()

    def get_client_by_email(self, email: str):
        with self.db_session() as session:
            client: Connection = session.get_client()
            cursor: Cursor = client.cursor()
            cursor.execute('SELECT * FROM Client WHERE email=%s', (email,))
            return cursor.fetchone()

    def get_client_by_phone(self, phone: str):
        with self.db_session() as session:
            client: Connection = session.get_client()
            cursor: Cursor = client.cursor()
            cursor.execute('SELECT * FROM Client WHERE phone=%s', (phone,))
            return cursor.fetchone()

    def create_client(self, client: ClientInput) -> bool:
        try:
            with self.db_session() as session:
                conn: Connection = session.get_client()
                cursor: Cursor = conn.cursor()
                cursor.execute('INSERT INTO Client(name, lastname, phone, address, email) VALUES(%s, %s, %s, %s, %s)',
                               (client.name, client.lastname, client.phone, client.address, client.email))
                return cursor.rowcount > 0
        except Exception:
            return False

    def update_client(self, id: int, client: ClientInput):
        try:
            with self.db_session() as session:
                conn: Connection = session.get_client()
                cursor: Cursor = conn.cursor()
                cursor.execute('UPDATE Client SET name=%s, lastname=%s, phone=%s, address=%s, email=%s WHERE id=%s',
                               (client.name, client.lastname, client.phone, client.address, client.email, id))
                return cursor.rowcount > 0
        except Exception:
            return False

    def delete_client(self, id):
        try:
            with self.db_session() as session:
                client: Connection = session.get_client()
                cursor: Cursor = client.cursor()
                cursor.execute('DELETE FROM Client WHERE id=%s',
                               (id,))
                return cursor.rowcount > 0
        except Exception:
            return False
