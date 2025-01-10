import container
from config import get_config
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from schemas import SaleInput

config = get_config()
sale_router = APIRouter(
    prefix=f'/api/{config.API_VERSION}/{config.DOMAIN}')


@sale_router.get('/sales', tags=['Sale'])
def get_sales() -> JSONResponse:
    with container.MainContainer.scope() as app:
        sale_controller = app.controllers.sale()
        return sale_controller.get_sales()


@sale_router.get('/sales/{id}', tags=['Sale'])
def get_sale_by_id(id: int) -> JSONResponse:
    with container.MainContainer.scope() as app:
        sale_controller = app.controllers.sale()
        return sale_controller.get_sale_by_id(id)


@sale_router.post('/sales', tags=['Sale'])
def create_sale(sale: SaleInput) -> JSONResponse:
    with container.MainContainer.scope() as app:
        sale_controller = app.controllers.sale()
        return sale_controller.create_sale(sale)


@sale_router.put('/sales/{id}', tags=['Sale'])
def update_sale(id: int, sale: SaleInput) -> JSONResponse:
    with container.MainContainer.scope() as app:
        sale_controller = app.controllers.sale()
        return sale_controller.update_sale(id, sale)


@sale_router.delete('/sales/{id}', tags=['Sale'])
def delete_sale(id: int) -> JSONResponse:
    with container.MainContainer.scope() as app:
        sale_controller = app.controllers.sale()
        return sale_controller.delete_sale(id)
