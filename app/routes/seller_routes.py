import container
from config import get_config
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from schemas import SellerInput

config = get_config()
seller_router = APIRouter(
    prefix=f'/api/{config.API_VERSION}/{config.DOMAIN}')


@seller_router.get('/sellers', tags=['Seller'])
def get_sellers() -> JSONResponse:
    with container.MainContainer.scope() as app:
        seller_controller = app.controllers.seller()
        return seller_controller.get_sellers()


@seller_router.get('/sellers/{id}', tags=['Seller'])
def get_seller_by_id(id: int) -> JSONResponse:
    with container.MainContainer.scope() as app:
        seller_controller = app.controllers.seller()
        return seller_controller.get_seller_by_id(id)


@seller_router.get('/sellers/phone/{phone}', tags=['Seller'])
def get_seller_by_phone(phone: str) -> JSONResponse:
    with container.MainContainer.scope() as app:
        seller_controller = app.controllers.seller()
        return seller_controller.get_seller_by_phone(phone)


@seller_router.post('/sellers', tags=['Seller'])
def create_seller(seller: SellerInput) -> JSONResponse:
    with container.MainContainer.scope() as app:
        seller_controller = app.controllers.seller()
        return seller_controller.create_seller(seller)


@seller_router.put('/sellers/{id}', tags=['Seller'])
def update_seller(id: int, seller: SellerInput) -> JSONResponse:
    with container.MainContainer.scope() as app:
        seller_controller = app.controllers.seller()
        return seller_controller.update_seller(id, seller)


@seller_router.delete('/sellers/{id}', tags=['Seller'])
def delete_seller(id: int) -> JSONResponse:
    with container.MainContainer.scope() as app:
        seller_controller = app.controllers.seller()
        return seller_controller.delete_seller(id)
