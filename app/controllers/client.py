import uuid
from datetime import datetime

from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas import ClientInput, ClientOutput
from services import IDatabaseClient


class ClientController:
    def __init__(self, db_service: IDatabaseClient) -> None:
        self.db_service = db_service
        self.transaction_id = str(uuid.uuid4())
        self.timestamp = datetime.now()
        self.response = {
            'meta': {'transaction_id': self.transaction_id, 'timestamp': self.timestamp}}

    def get_clients(self) -> JSONResponse:
        rows = self.db_service.get_clients()

        self.response['clients'] = [ClientOutput(
            id=row[0], name=row[1], lastname=row[2],
            phone=row[3], address=row[4], email=row[5]) for row in rows]

        return JSONResponse(jsonable_encoder(self.response), status.HTTP_200_OK)

    def get_client_by_id(self, id: int) -> JSONResponse:
        client = self.db_service.get_client_by_id(id)

        if not client:
            self.response['message'] = f'Client with id {id} not found'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_404_NOT_FOUND)

        self.response['client'] = ClientOutput(
            id=client[0], name=client[1], lastname=client[2],
            phone=client[3], address=client[4], email=client[5])
        return JSONResponse(jsonable_encoder(self.response), status.HTTP_200_OK)

    def get_client_by_phone(self, phone: str) -> JSONResponse:
        client = self.db_service.get_client_by_phone(phone)

        if not client:
            self.response['message'] = f'Client with phone {phone} not found'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_404_NOT_FOUND)

        self.response['client'] = ClientOutput(
            id=client[0], name=client[1], lastname=client[2],
            phone=client[3], address=client[4], email=client[5])
        return JSONResponse(jsonable_encoder(self.response), status.HTTP_200_OK)

    def get_client_by_email(self, email: str) -> JSONResponse:
        client = self.db_service.get_client_by_email(email)

        if not client:
            self.response['message'] = f'Client with email {email} not found'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_404_NOT_FOUND)

        self.response['client'] = ClientOutput(
            id=client[0], name=client[1], lastname=client[2],
            phone=client[3], address=client[4], email=client[5])
        return JSONResponse(jsonable_encoder(self.response), status.HTTP_200_OK)

    def create_client(self, client: ClientInput) -> JSONResponse:
        client_db = self.db_service.get_client_by_email(client.email)

        if client_db:
            self.response['message'] = f'Client {
                client.name} already exists.'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_409_CONFLICT)

        if not self.db_service.create_client(client):
            self.response['message'] = f'Error while inserting client {
                client.name}'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_500_INTERNAL_SERVER_ERROR)

        self.response['message'] = 'Client inserted successfully'
        return JSONResponse(jsonable_encoder(self.response), status.HTTP_201_CREATED)

    def update_client(self, id: int, client: ClientInput) -> JSONResponse:
        client_db = self.db_service.get_client_by_id(id)

        if not client_db:
            self.response['message'] = f'Client with id {id} not found'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_404_NOT_FOUND)

        if not self.db_service.update_client(id, client):
            self.response['message'] = f'Error while updating client {
                client.name} or there is nothing to update'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_500_INTERNAL_SERVER_ERROR)

        self.response['message'] = 'Client updated successfully'
        return self.response

    def delete_client(self, id: int) -> JSONResponse:
        client_db = self.db_service.get_client_by_id(id)

        if not client_db:
            self.response['message'] = f'Client with id {id} not found'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_404_NOT_FOUND)

        if not self.db_service.delete_client(id):
            self.response['message'] = f'Error while deleting client {id}'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_500_INTERNAL_SERVER_ERROR)

        self.response['message'] = 'Client deleted successfully'
        return self.response
