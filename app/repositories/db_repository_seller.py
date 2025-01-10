from pymysql import Connection
from pymysql.cursors import Cursor
from schemas import SellerInput
from services import IDatabaseSeller


class DBRepositorySeller(IDatabaseSeller):
    def __init__(self, db_session) -> None:
        self.db_session = db_session

    def get_sellers(self):
        with self.db_session() as session:
            client: Connection = session.get_client()
            cursor: Cursor = client.cursor()
            cursor.execute('SELECT * FROM Seller')
            return cursor.fetchall()

    def get_seller_by_id(self, id: int):
        with self.db_session() as session:
            client: Connection = session.get_client()
            cursor: Cursor = client.cursor()
            cursor.execute('SELECT * FROM Seller WHERE id=%s', (id,))
            return cursor.fetchone()

    def get_seller_by_phone(self, phone: str):
        with self.db_session() as session:
            client: Connection = session.get_client()
            cursor: Cursor = client.cursor()
            cursor.execute('SELECT * FROM Seller WHERE phone=%s', (phone,))
            return cursor.fetchone()

    def create_seller(self, seller: SellerInput) -> bool:
        try:
            with self.db_session() as session:
                client: Connection = session.get_client()
                cursor: Cursor = client.cursor()
                cursor.execute('INSERT INTO Seller(name, lastname, phone, address, company) VALUES(%s, %s, %s, %s, %s)',
                               (seller.name, seller.lastname, seller.phone, seller.address, seller.company))
                return cursor.rowcount > 0
        except Exception:
            return False

    def update_seller(self, id: int, seller: SellerInput):
        try:
            with self.db_session() as session:
                client: Connection = session.get_client()
                cursor: Cursor = client.cursor()
                cursor.execute('UPDATE Seller SET name=%s, lastname=%s, phone=%s, address=%s, company=%s WHERE id=%s',
                               (seller.name, seller.lastname, seller.phone, seller.address, seller.company, id))
                return cursor.rowcount > 0
        except Exception:
            return False

    def delete_seller(self, id):
        try:
            with self.db_session() as session:
                client: Connection = session.get_client()
                cursor: Cursor = client.cursor()
                cursor.execute('DELETE FROM Seller WHERE id=%s',
                               (id,))
                return cursor.rowcount > 0
        except Exception:
            return False
