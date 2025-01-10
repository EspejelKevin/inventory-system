import container
from config import get_config
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from schemas import CategoryInput

config = get_config()
category_router = APIRouter(
    prefix=f'/api/{config.API_VERSION}/{config.DOMAIN}')


@category_router.get('/categories', tags=['Category'])
def get_categories() -> JSONResponse:
    with container.MainContainer.scope() as app:
        category_controller = app.controllers.category()
        return category_controller.get_categories()


@category_router.get('/categories/{id}', tags=['Category'])
def get_category_by_id(id: int) -> JSONResponse:
    with container.MainContainer.scope() as app:
        category_controller = app.controllers.category()
        return category_controller.get_category_by_id(id)


@category_router.post('/categories', tags=['Category'])
def create_category(category: CategoryInput) -> JSONResponse:
    with container.MainContainer.scope() as app:
        category_controller = app.controllers.category()
        return category_controller.create_category(category)


@category_router.put('/categories/{id}', tags=['Category'])
def update_category(id: int, category: CategoryInput) -> JSONResponse:
    with container.MainContainer.scope() as app:
        category_controller = app.controllers.category()
        return category_controller.update_category(id, category)


@category_router.delete('/categories/{id}', tags=['Category'])
def delete_category(id: int) -> JSONResponse:
    with container.MainContainer.scope() as app:
        category_controller = app.controllers.category()
        return category_controller.delete_category(id)
