from pymysql import Connection
from pymysql.cursors import Cursor
from schemas import ProductInput
from services import IDatabaseProduct


class DBRepositoryProduct(IDatabaseProduct):
    def __init__(self, db_session) -> None:
        self.db_session = db_session

    def get_products(self):
        with self.db_session() as session:
            client: Connection = session.get_client()
            cursor: Cursor = client.cursor()
            query = """
                SELECT p.id, p.name, p.description, p.cost, p.price, p.stock, p.sku, c.name
                FROM product as p 
                INNER JOIN category as c
                ON p.category_id = c.id;
            """
            cursor.execute(query)
            return cursor.fetchall()

    def get_product_by_id(self, id):
        with self.db_session() as session:
            client: Connection = session.get_client()
            cursor: Cursor = client.cursor()
            query = """
                SELECT p.id, p.name, p.description, p.cost, p.price, p.stock, p.sku, c.name
                FROM product as p 
                INNER JOIN category as c
                ON p.category_id = c.id
                WHERE p.id=%s;
            """
            cursor.execute(query, (id,))
            return cursor.fetchone()

    def get_product_by_sku(self, sku):
        with self.db_session() as session:
            client: Connection = session.get_client()
            cursor: Cursor = client.cursor()
            cursor.execute('SELECT * FROM Product WHERE sku=%s', (sku,))
            return cursor.fetchone()

    def create_product(self, product: ProductInput):
        try:
            with self.db_session() as session:
                client: Connection = session.get_client()
                cursor: Cursor = client.cursor()
                query = """
                    INSERT INTO Product(name, description, cost, price, stock, sku, category_id)
                    VALUES(%s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query,
                               (product.name, product.description, product.cost,
                                product.price, product.stock, product.sku, product.category_id))
                return cursor.rowcount > 0
        except Exception:
            return False

    def update_product(self, id: int, product: ProductInput):
        try:
            with self.db_session() as session:
                client: Connection = session.get_client()
                cursor: Cursor = client.cursor()
                query = """
                    UPDATE Product SET 
                    name=%s, description=%s, 
                    cost=%s, price=%s, stock=%s,
                    sku=%s, category_id=%s 
                    WHERE id=%s
                """
                cursor.execute(query, (product.name, product.description, product.cost,
                                       product.price, product.stock, product.sku, product.category_id, id))
                return cursor.rowcount > 0
        except Exception:
            return False

    def delete_product(self, id: int):
        try:
            with self.db_session() as session:
                client: Connection = session.get_client()
                cursor: Cursor = client.cursor()
                cursor.execute('DELETE FROM Product WHERE id=%s', (id,))
                return cursor.rowcount > 0
        except Exception:
            return False
