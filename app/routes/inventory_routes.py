import container
from config import get_config
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from schemas import InventoryInput

config = get_config()
inventory_router = APIRouter(
    prefix=f'/api/{config.API_VERSION}/{config.DOMAIN}')


@inventory_router.get('/inventories', tags=['Inventory'])
def get_inventories() -> JSONResponse:
    with container.MainContainer.scope() as app:
        inventory_controller = app.controllers.inventory()
        return inventory_controller.get_inventories()


@inventory_router.get('/inventories/{id}', tags=['Inventory'])
def get_inventory_by_id(id: int) -> JSONResponse:
    with container.MainContainer.scope() as app:
        inventory_controller = app.controllers.inventory()
        return inventory_controller.get_inventory_by_id(id)


@inventory_router.get('/inventories/code/{code}', tags=['Inventory'])
def get_inventory_by_code(code: str) -> JSONResponse:
    with container.MainContainer.scope() as app:
        inventory_controller = app.controllers.inventory()
        return inventory_controller.get_inventory_by_code(code)


@inventory_router.post('/inventories', tags=['Inventory'])
def create_inventory(inventory: InventoryInput) -> JSONResponse:
    with container.MainContainer.scope() as app:
        inventory_controller = app.controllers.inventory()
        return inventory_controller.create_inventory(inventory)


@inventory_router.put('/inventories/{id}', tags=['Inventory'])
def update_inventory(id: int, inventory: InventoryInput) -> JSONResponse:
    with container.MainContainer.scope() as app:
        inventory_controller = app.controllers.inventory()
        return inventory_controller.update_inventory(id, inventory)


@inventory_router.delete('/inventories/{id}', tags=['Inventory'])
def delete_inventory(id: int) -> JSONResponse:
    with container.MainContainer.scope() as app:
        inventory_controller = app.controllers.inventory()
        return inventory_controller.delete_inventory(id)
