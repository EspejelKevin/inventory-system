import container
import uvicorn
from config import get_config
from fastapi import FastAPI
from routes import (category_router, client_router, healthcheck_router,
                    inventory_router, product_router, seller_router)

tags = [
    {
        'name': 'Health Check',
        'description': 'Endpoints to check service availability.'
    },
    {
        'name': 'Category',
        'description': 'Operations CRUD to categories.'
    },
    {
        'name': 'Product',
        'description': 'Operations CRUD to products.'
    },
    {
        'name': 'Client',
        'description': 'Operations CRUD to clients.'
    },
    {
        'name': 'Seller',
        'description': 'Operations CRUD to sellers.'
    },
    {
        'name': 'Inventory',
        'description': 'Operations CRUD to inventories.'
    },
    {
        'name': 'Sale',
        'description': 'Operations CRUD to sales.'
    }
]

config = get_config()


def on_startup():
    container.MainContainer.init()


app = FastAPI(title=config.TITLE,
              summary='Sales system to manage users, sales and products.',
              description='API RESTful to manage operations CRUD of users, products and sales.',
              version=config.APP_VERSION,
              openapi_tags=tags,
              on_startup=[on_startup])
app.include_router(healthcheck_router)
app.include_router(category_router)
app.include_router(product_router)
app.include_router(client_router)
app.include_router(seller_router)
app.include_router(inventory_router)


if __name__ == '__main__':
    uvicorn.run('main:app', host=config.HOST,
                port=config.PORT, reload=config.RELOAD)
