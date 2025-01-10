import container
from config import get_config
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from schemas import ProductInput

config = get_config()
product_router = APIRouter(
    prefix=f'/api/{config.API_VERSION}/{config.DOMAIN}')


@product_router.get('/products', tags=['Product'])
def get_products() -> JSONResponse:
    with container.MainContainer.scope() as app:
        product_controller = app.controllers.product()
        return product_controller.get_products()


@product_router.get('/products/{id}', tags=['Product'])
def get_product_by_id(id: int) -> JSONResponse:
    with container.MainContainer.scope() as app:
        product_controller = app.controllers.product()
        return product_controller.get_product_by_id(id)


@product_router.post('/products', tags=['Product'])
def create_product(product: ProductInput) -> JSONResponse:
    with container.MainContainer.scope() as app:
        product_controller = app.controllers.product()
        return product_controller.create_product(product)


@product_router.put('/products/{id}', tags=['Product'])
def update_product(id: int, product: ProductInput) -> JSONResponse:
    with container.MainContainer.scope() as app:
        product_controller = app.controllers.product()
        return product_controller.update_product(id, product)


@product_router.delete('/products/{id}', tags=['Product'])
def delete_product(id: int) -> JSONResponse:
    with container.MainContainer.scope() as app:
        product_controller = app.controllers.product()
        return product_controller.delete_product(id)
