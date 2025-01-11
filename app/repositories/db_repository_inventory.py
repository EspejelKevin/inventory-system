from pymysql import Connection
from pymysql.cursors import Cursor
from schemas import InventoryInput
from services import IDatabaseInventory


class DBRepositoryInventory(IDatabaseInventory):
    def __init__(self, db_session) -> None:
        self.db_session = db_session

    def get_inventories(self):
        with self.db_session() as session:
            client: Connection = session.get_client()
            cursor: Cursor = client.cursor()
            query = """
                SELECT i.id, i.quantity, i.update_date, i.description, i.movement_type, p.name, i.code
                FROM inventory as i 
                INNER JOIN product as p
                ON i.product_id = p.id;
            """
            cursor.execute(query)
            return cursor.fetchall()

    def get_inventory_by_id(self, id: int):
        with self.db_session() as session:
            client: Connection = session.get_client()
            cursor: Cursor = client.cursor()
            query = """
                SELECT i.id, i.quantity, i.update_date, i.description, i.movement_type, p.name, i.code
                FROM inventory as i 
                INNER JOIN product as p
                ON i.product_id = p.id
                WHERE i.id=%s;
            """
            cursor.execute(query, (id,))
            return cursor.fetchone()

    def get_inventory_by_code(self, code: str):
        with self.db_session() as session:
            client: Connection = session.get_client()
            cursor: Cursor = client.cursor()
            query = """
                SELECT i.id, i.quantity, i.update_date, i.description, i.movement_type, p.name, i.code
                FROM inventory as i 
                INNER JOIN product as p
                ON i.product_id = p.id
                WHERE i.code=%s;
            """
            cursor.execute(query, (code,))
            return cursor.fetchone()

    def create_inventory(self, inventory: InventoryInput) -> bool:
        try:
            with self.db_session() as session:
                conn: Connection = session.get_client()
                cursor: Cursor = conn.cursor()
                query = """
                    INSERT INTO Inventory(quantity, update_date, description, movement_type, product_id, code)
                    VALUES(%s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query,
                               (inventory.quantity, inventory.update_date, inventory.description,
                                inventory.movement_type, inventory.product_id, inventory.code))
                return cursor.rowcount > 0
        except Exception:
            return False

    def update_inventory(self, id: int, inventory: InventoryInput):
        try:
            with self.db_session() as session:
                conn: Connection = session.get_client()
                cursor: Cursor = conn.cursor()
                query = """
                    UPDATE Inventory SET quantity=%s, update_date=%s, description=%s, movement_type=%s,
                    product_id=%s, code=%s
                    WHERE id=%s
                """
                cursor.execute(query,
                               (inventory.quantity, inventory.update_date, inventory.description,
                                inventory.movement_type, inventory.product_id, inventory.code, id))
                return cursor.rowcount > 0
        except Exception:
            return False

    def delete_inventory(self, id):
        try:
            with self.db_session() as session:
                client: Connection = session.get_client()
                cursor: Cursor = client.cursor()
                cursor.execute('DELETE FROM Inventory WHERE id=%s',
                               (id,))
                return cursor.rowcount > 0
        except Exception:
            return False
