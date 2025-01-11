from contextlib import contextmanager
from typing import Optional

from config import Config
from controllers import (CategoryController, ClientController,
                         InventoryController, ProductController,
                         ReadinessController, SellerController)
from database import Database
from dependency_injector import containers, providers
from repositories import (DBRepositoryCategory, DBRepositoryClient,
                          DBRepositoryHealthCheck, DBRepositoryInventory,
                          DBRepositoryProduct, DBRepositorySeller)
from services import (DBServiceCategory, DBServiceClient, DBServiceHealthCheck,
                      DBServiceInventory, DBServiceProduct, DBServiceSeller)


class ContainerDatabases(containers.DeclarativeContainer):
    config = providers.Dependency(Config)
    mysql = providers.Singleton(Database, host=config.provided.DB_HOST, user=config.provided.DB_USER,
                                password=config.provided.DB_PASS, db=config.provided.DB_NAME)


class ContainerRepositories(containers.DeclarativeContainer):
    databases: ContainerDatabases = providers.DependenciesContainer()
    db_repository_category = providers.Singleton(
        DBRepositoryCategory, db_session=databases.mysql.provided.session)
    db_repository_healthcheck = providers.Singleton(
        DBRepositoryHealthCheck, db_session=databases.mysql.provided.session)
    db_repository_product = providers.Singleton(
        DBRepositoryProduct, db_session=databases.mysql.provided.session)
    db_repository_client = providers.Singleton(
        DBRepositoryClient, db_session=databases.mysql.provided.session)
    db_repository_seller = providers.Singleton(
        DBRepositorySeller, db_session=databases.mysql.provided.session)
    db_repository_inventory = providers.Singleton(
        DBRepositoryInventory, db_session=databases.mysql.provided.session)


class ContainerServices(containers.DeclarativeContainer):
    repositories: ContainerRepositories = providers.DependenciesContainer()
    db_service_category = providers.Factory(
        DBServiceCategory, db_repository=repositories.db_repository_category)
    db_service_healthcheck = providers.Factory(
        DBServiceHealthCheck, db_repository=repositories.db_repository_healthcheck)
    db_service_product = providers.Factory(
        DBServiceProduct, db_repository=repositories.db_repository_product)
    db_service_client = providers.Factory(
        DBServiceClient, db_repository=repositories.db_repository_client)
    db_service_seller = providers.Factory(
        DBServiceSeller, db_repository=repositories.db_repository_seller)
    db_service_inventory = providers.Factory(
        DBServiceInventory, db_repository=repositories.db_repository_inventory)


class ContainerControllers(containers.DeclarativeContainer):
    services: ContainerServices = providers.DependenciesContainer()
    readiness = providers.Factory(
        ReadinessController, db_service=services.db_service_healthcheck)
    category = providers.Factory(
        CategoryController, db_service=services.db_service_category)
    product = providers.Factory(
        ProductController, db_service=services.db_service_product
    )
    client = providers.Factory(
        ClientController, db_service=services.db_service_client
    )
    seller = providers.Factory(
        SellerController, db_service=services.db_service_seller
    )
    inventory = providers.Factory(
        InventoryController, db_service=services.db_service_inventory
    )


class AppContainer(containers.DeclarativeContainer):
    config = providers.ThreadSafeSingleton(Config)
    databases = providers.Container(ContainerDatabases, config=config)
    repositories = providers.Container(
        ContainerRepositories, databases=databases)
    services = providers.Container(
        ContainerServices, repositories=repositories)
    controllers = providers.Container(ContainerControllers, services=services)


class MainContainer:

    container: Optional[AppContainer] = None

    @classmethod
    @contextmanager
    def scope(cls):
        try:
            cls.container.services.init_resources()
            yield cls.container
        finally:
            cls.container.services.shutdown_resources()

    @classmethod
    def init(cls) -> None:
        if cls.container is None:
            cls.container = AppContainer()
