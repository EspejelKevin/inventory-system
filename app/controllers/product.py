import uuid
from datetime import datetime

from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas import Product, ProductInput, ProductOutput
from services import IDatabaseProduct


class ProductController:
    def __init__(self, db_service: IDatabaseProduct) -> None:
        self.db_service = db_service
        self.transaction_id = str(uuid.uuid4())
        self.timestamp = datetime.now()
        self.response = {
            'meta': {'transaction_id': self.transaction_id, 'timestamp': self.timestamp}}

    def get_products(self) -> JSONResponse:
        rows = self.db_service.get_products()
        self.response['products'] = [ProductOutput(
            id=row[0], name=row[1], description=row[2], cost=row[3],
            price=row[4], stock=row[5], sku=row[6], category=row[7]) for row in rows]

        return JSONResponse(jsonable_encoder(self.response), status.HTTP_200_OK)

    def get_product_by_id(self, id: int) -> JSONResponse:
        product = self.db_service.get_product_by_id(id)

        if not product:
            self.response['message'] = f'Product with id {id} not found'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_404_NOT_FOUND)

        self.response['product'] = ProductOutput(
            id=product[0], name=product[1], description=product[2], cost=product[3],
            price=product[4], stock=product[5], sku=product[6], category=product[7])
        return JSONResponse(jsonable_encoder(self.response), status.HTTP_200_OK)

    def create_product(self, product: ProductInput) -> JSONResponse:
        product_db = self.db_service.get_product_by_name(product.name)

        if product_db:
            self.response['message'] = f'Product {
                product.name} already exists.'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_409_CONFLICT)

        product = Product(**product.model_dump(), sku=str(uuid.uuid4())[0:8])
        if not self.db_service.create_product(product):
            self.response['message'] = f'Error while inserting product {
                product.name}'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_500_INTERNAL_SERVER_ERROR)

        self.response['message'] = 'Product inserted successfully'
        return JSONResponse(jsonable_encoder(self.response), status.HTTP_201_CREATED)

    def update_product(self, id: int, product: ProductInput) -> JSONResponse:
        product_db = self.db_service.get_product_by_id(id)

        if not product_db:
            self.response['message'] = f'Product with id {id} not found'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_404_NOT_FOUND)

        if not self.db_service.update_product(id, product):
            self.response['message'] = f'Error while updating product {
                product.name} or there is nothing to update'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_500_INTERNAL_SERVER_ERROR)

        self.response['message'] = 'Product updated successfully'
        return JSONResponse(jsonable_encoder(self.response), status.HTTP_200_OK)

    def delete_product(self, id: int) -> JSONResponse:
        product_db = self.db_service.get_product_by_id(id)

        if not product_db:
            self.response['message'] = f'Product with id {id} not found'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_404_NOT_FOUND)

        if not self.db_service.delete_product(id):
            self.response['message'] = f'Error while deleting product {id}'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_500_INTERNAL_SERVER_ERROR)

        self.response['message'] = 'Product deleted successfully'
        return JSONResponse(jsonable_encoder(self.response), status.HTTP_200_OK)
