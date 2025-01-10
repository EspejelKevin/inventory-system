import container
from config import get_config
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

config = get_config()
healthcheck_router = APIRouter(
    prefix=f'/api/{config.API_VERSION}/{config.DOMAIN}')


@healthcheck_router.get('/liveness', tags=['Health Check'])
def liveness() -> JSONResponse:
    return JSONResponse(content={'status': 'service is up'},
                        status_code=status.HTTP_200_OK)


@healthcheck_router.get('/readiness', tags=['Health Check'])
def readiness() -> JSONResponse:
    with container.MainContainer.scope() as app:
        readiness_controller = app.controllers.readiness()
        return readiness_controller.execute()
