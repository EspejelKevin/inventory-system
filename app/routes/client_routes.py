import container
from config import get_config
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from schemas import ClientInput

config = get_config()
client_router = APIRouter(
    prefix=f'/api/{config.API_VERSION}/{config.DOMAIN}')


@client_router.get('/clients', tags=['Client'])
def get_clients() -> JSONResponse:
    with container.MainContainer.scope() as app:
        client_controller = app.controllers.client()
        return client_controller.get_clients()


@client_router.get('/clients/{id}', tags=['Client'])
def get_client_by_id(id: int) -> JSONResponse:
    with container.MainContainer.scope() as app:
        client_controller = app.controllers.client()
        return client_controller.get_client_by_id(id)


@client_router.get('/clients/email/{email}', tags=['Client'])
def get_client_by_email(email: str) -> JSONResponse:
    with container.MainContainer.scope() as app:
        client_controller = app.controllers.client()
        return client_controller.get_client_by_email(email)


@client_router.get('/clients/phone/{phone}', tags=['Client'])
def get_client_by_phone(phone: str) -> JSONResponse:
    with container.MainContainer.scope() as app:
        client_controller = app.controllers.client()
        return client_controller.get_client_by_phone(phone)


@client_router.post('/clients', tags=['Client'])
def create_client(client: ClientInput) -> JSONResponse:
    with container.MainContainer.scope() as app:
        client_controller = app.controllers.client()
        return client_controller.create_client(client)


@client_router.put('/clients/{id}', tags=['Client'])
def update_client(id: int, client: ClientInput) -> JSONResponse:
    with container.MainContainer.scope() as app:
        client_controller = app.controllers.client()
        return client_controller.update_client(id, client)


@client_router.delete('/clients/{id}', tags=['Client'])
def delete_client(id: int) -> JSONResponse:
    with container.MainContainer.scope() as app:
        client_controller = app.controllers.client()
        return client_controller.delete_client(id)
