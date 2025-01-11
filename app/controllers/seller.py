import uuid
from datetime import datetime

from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas import SellerInput, SellerOutput
from services import IDatabaseSeller


class SellerController:
    def __init__(self, db_service: IDatabaseSeller) -> None:
        self.db_service = db_service
        self.transaction_id = str(uuid.uuid4())
        self.timestamp = datetime.now()
        self.response = {
            'meta': {'transaction_id': self.transaction_id, 'timestamp': self.timestamp}}

    def get_sellers(self):
        rows = self.db_service.get_sellers()

        self.response['sellers'] = [SellerOutput(
            id=row[0], name=row[1], lastname=row[2], phone=row[3], address=row[4], company=row[5]) for row in rows]

        return JSONResponse(jsonable_encoder(self.response), status.HTTP_200_OK)

    def get_seller_by_id(self, id: int) -> JSONResponse:
        seller = self.db_service.get_seller_by_id(id)

        if not seller:
            self.response['message'] = f'Seller with id {id} not found'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_404_NOT_FOUND)

        self.response['seller'] = SellerOutput(
            id=seller[0], name=seller[1], lastname=seller[2], phone=seller[3], address=seller[4], company=seller[5])
        return JSONResponse(jsonable_encoder(self.response), status.HTTP_200_OK)

    def get_seller_by_phone(self, phone: str) -> JSONResponse:
        seller = self.db_service.get_seller_by_phone(phone)

        if not seller:
            self.response['message'] = f'Seller with phone {phone} not found'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_404_NOT_FOUND)

        self.response['seller'] = SellerOutput(
            id=seller[0], name=seller[1], lastname=seller[2], phone=seller[3], address=seller[4], company=seller[5])
        return JSONResponse(jsonable_encoder(self.response), status.HTTP_200_OK)

    def create_seller(self, seller: SellerInput) -> JSONResponse:
        seller_db = self.db_service.get_seller_by_phone(seller.phone)

        if seller_db:
            self.response['message'] = f'Seller {
                seller.name} already exists.'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_409_CONFLICT)

        if not self.db_service.create_seller(seller):
            self.response['message'] = f'Error while inserting seller {
                seller.name}'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_500_INTERNAL_SERVER_ERROR)

        self.response['message'] = 'Seller inserted successfully'
        return JSONResponse(jsonable_encoder(self.response), status.HTTP_201_CREATED)

    def update_seller(self, id: int, seller: SellerInput) -> JSONResponse:
        seller_db = self.db_service.get_seller_by_id(id)

        if not seller_db:
            self.response['message'] = f'Seller with id {id} not found'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_404_NOT_FOUND)

        if not self.db_service.update_seller(id, seller):
            self.response['message'] = f'Error while updating seller {
                seller.name} or there is nothing to update'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_500_INTERNAL_SERVER_ERROR)

        self.response['message'] = 'Seller updated successfully'
        return self.response

    def delete_seller(self, id: int) -> JSONResponse:
        seller_db = self.db_service.get_seller_by_id(id)

        if not seller_db:
            self.response['message'] = f'Seller with id {id} not found'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_404_NOT_FOUND)

        if not self.db_service.delete_seller(id):
            self.response['message'] = f'Error while deleting seller {id}'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_500_INTERNAL_SERVER_ERROR)

        self.response['message'] = 'Seller deleted successfully'
        return self.response
