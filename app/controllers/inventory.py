import uuid
from datetime import datetime

from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas import InventoryInput, InventoryOutput
from services import IDatabaseInventory


class InventoryController:
    def __init__(self, db_service: IDatabaseInventory) -> None:
        self.db_service = db_service
        self.transaction_id = str(uuid.uuid4())
        self.timestamp = datetime.now()
        self.response = {
            'meta': {'transaction_id': self.transaction_id, 'timestamp': self.timestamp}}

    def get_inventories(self):
        rows = self.db_service.get_inventories()

        self.response['inventories'] = [InventoryOutput(
            id=row[0], quantity=row[1], update_date=row[2],
            description=row[3], movement_type=row[4], product=row[5], code=row[6]) for row in rows]

        return JSONResponse(jsonable_encoder(self.response), status.HTTP_200_OK)

    def get_inventory_by_id(self, id: int) -> JSONResponse:
        inventory = self.db_service.get_inventory_by_id(id)

        if not inventory:
            self.response['message'] = f'Inventory with id {id} not found'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_404_NOT_FOUND)

        self.response['inventory'] = InventoryOutput(
            id=inventory[0], quantity=inventory[1], update_date=inventory[2],
            description=inventory[3], movement_type=inventory[4], product=inventory[5], code=inventory[6])
        return JSONResponse(jsonable_encoder(self.response), status.HTTP_200_OK)

    def get_inventory_by_code(self, code: str) -> JSONResponse:
        inventory = self.db_service.get_inventory_by_code(code)

        if not inventory:
            self.response['message'] = f'Inventory with code {code} not found'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_404_NOT_FOUND)

        self.response['inventory'] = InventoryOutput(
            id=inventory[0], quantity=inventory[1], update_date=inventory[2],
            description=inventory[3], movement_type=inventory[4], product=inventory[5], code=inventory[6])
        return JSONResponse(jsonable_encoder(self.response), status.HTTP_200_OK)

    def create_inventory(self, inventory: InventoryInput) -> JSONResponse:
        inventory_db = self.db_service.get_inventory_by_code(inventory.code)

        if inventory_db:
            self.response['message'] = f'Inventory {
                inventory.code} already exists.'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_409_CONFLICT)

        if not self.db_service.create_inventory(inventory):
            self.response['message'] = f'Error while inserting inventory {
                inventory.code}'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_500_INTERNAL_SERVER_ERROR)

        self.response['message'] = 'Inventory inserted successfully'
        return JSONResponse(jsonable_encoder(self.response), status.HTTP_201_CREATED)

    def update_inventory(self, id: int, inventory: InventoryInput) -> JSONResponse:
        inventory_db = self.db_service.get_inventory_by_id(id)

        if not inventory_db:
            self.response['message'] = f'Inventory with id {id} not found'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_404_NOT_FOUND)

        if not self.db_service.update_inventory(id, inventory):
            self.response['message'] = f'Error while updating inventory {
                inventory.code} or there is nothing to update'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_500_INTERNAL_SERVER_ERROR)

        self.response['message'] = 'Inventory updated successfully'
        return self.response

    def delete_inventory(self, id: int) -> JSONResponse:
        inventory_db = self.db_service.get_inventory_by_id(id)

        if not inventory_db:
            self.response['message'] = f'Inventory with id {id} not found'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_404_NOT_FOUND)

        if not self.db_service.delete_inventory(id):
            self.response['message'] = f'Error while deleting inventory {id}'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_500_INTERNAL_SERVER_ERROR)

        self.response['message'] = 'Inventory deleted successfully'
        return self.response
