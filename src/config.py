from functools import lru_cache
from os import getenv

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    db_user: str = getenv('DB_USER')
    db_password: str = getenv('DB_PASSWORD')
    db_name: str = getenv('DB_NAME')
    db_host: str = getenv('DB_HOST')
    db_port: int = getenv('DB_PORT')

    @property
    def db_config(self) -> str:
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"


@lru_cache
def get_settings():
    return Settings()
