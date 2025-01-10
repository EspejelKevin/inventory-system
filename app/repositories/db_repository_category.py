from pymysql import Connection
from pymysql.cursors import Cursor
from schemas import CategoryInput
from services import IDatabaseCategory


class DBRepositoryCategory(IDatabaseCategory):
    def __init__(self, db_session) -> None:
        self.db_session = db_session

    def get_categories(self):
        with self.db_session() as session:
            client: Connection = session.get_client()
            cursor: Cursor = client.cursor()
            cursor.execute('SELECT * FROM Category')
            return cursor.fetchall()

    def get_category_by_id(self, id: int):
        with self.db_session() as session:
            client: Connection = session.get_client()
            cursor: Cursor = client.cursor()
            cursor.execute('SELECT * FROM Category WHERE id=%s', (id,))
            return cursor.fetchone()

    def get_category_by_name(self, name: str):
        with self.db_session() as session:
            client: Connection = session.get_client()
            cursor: Cursor = client.cursor()
            cursor.execute('SELECT * FROM Category WHERE name=%s', (name,))
            return cursor.fetchone()

    def create_category(self, category: CategoryInput) -> bool:
        try:
            with self.db_session() as session:
                client: Connection = session.get_client()
                cursor: Cursor = client.cursor()
                cursor.execute('INSERT INTO Category(name, description) VALUES(%s, %s)',
                               (category.name, category.description))
                return cursor.rowcount > 0
        except Exception:
            return False

    def update_category(self, id: int, category: CategoryInput):
        try:
            with self.db_session() as session:
                client: Connection = session.get_client()
                cursor: Cursor = client.cursor()
                cursor.execute('UPDATE Category SET name=%s, description=%s WHERE id=%s',
                               (category.name, category.description, id))
                return cursor.rowcount > 0
        except Exception:
            return False

    def delete_category(self, id):
        try:
            with self.db_session() as session:
                client: Connection = session.get_client()
                cursor: Cursor = client.cursor()
                cursor.execute('DELETE FROM Category WHERE id=%s',
                               (id,))
                return cursor.rowcount > 0
        except Exception:
            return False
