import uuid
from datetime import datetime

from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas import CategoryInput, CategoryOutput
from services import IDatabaseCategory


class CategoryController:
    def __init__(self, db_service: IDatabaseCategory) -> None:
        self.db_service = db_service
        self.transaction_id = str(uuid.uuid4())
        self.timestamp = datetime.now()
        self.response = {
            'meta': {'transaction_id': self.transaction_id, 'timestamp': self.timestamp}}

    def get_categories(self) -> JSONResponse:
        rows = self.db_service.get_categories()

        self.response['categories'] = [CategoryOutput(
            id=row[0], name=row[1], description=row[2]) for row in rows]

        return JSONResponse(jsonable_encoder(self.response), status.HTTP_200_OK)

    def get_category_by_id(self, id: int) -> JSONResponse:
        category = self.db_service.get_category_by_id(id)

        if not category:
            self.response['message'] = f'Category with id {id} not found'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_404_NOT_FOUND)

        self.response['category'] = CategoryOutput(
            id=category[0], name=category[1], description=category[2])
        return JSONResponse(jsonable_encoder(self.response), status.HTTP_200_OK)

    def create_category(self, category: CategoryInput) -> JSONResponse:
        category_db = self.db_service.get_category_by_name(category.name)

        if category_db:
            self.response['message'] = f'Category {
                category.name} already exists.'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_409_CONFLICT)

        if not self.db_service.create_category(category):
            self.response['message'] = f'Error while inserting category {
                category.name}'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_500_INTERNAL_SERVER_ERROR)

        self.response['message'] = 'Category inserted successfully'
        return JSONResponse(jsonable_encoder(self.response), status.HTTP_201_CREATED)

    def update_category(self, id: int, category: CategoryInput) -> JSONResponse:
        category_db = self.db_service.get_category_by_id(id)

        if not category_db:
            self.response['message'] = f'Category with id {id} not found'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_404_NOT_FOUND)

        if not self.db_service.update_category(id, category):
            self.response['message'] = f'Error while updating category {
                category.name} or there is nothing to update'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_500_INTERNAL_SERVER_ERROR)

        self.response['message'] = 'Category updated successfully'
        return self.response

    def delete_category(self, id: int) -> JSONResponse:
        category_db = self.db_service.get_category_by_id(id)

        if not category_db:
            self.response['message'] = f'Category with id {id} not found'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_404_NOT_FOUND)

        if not self.db_service.delete_category(id):
            self.response['message'] = f'Error while deleting category {id}'
            return JSONResponse(jsonable_encoder(self.response), status.HTTP_500_INTERNAL_SERVER_ERROR)

        self.response['message'] = 'Category deleted successfully'
        return self.response
