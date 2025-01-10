from functools import cache

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    PORT: int = 8000
    HOST: str = '0.0.0.0'
    RELOAD: bool = False
    API_VERSION: str = 'v1'
    DOMAIN: str
    TITLE: str
    APP_VERSION: str

    DB_HOST: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str


@cache
def get_config() -> Config:
    return Config()
