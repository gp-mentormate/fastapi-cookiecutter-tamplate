from functools import lru_cache

from decouple import config
from pydantic import BaseSettings


class Settings(BaseSettings):
    db_user: str = config('DB_USER', cast=str)
    db_password: str = config('DB_PASSWORD', cast=str)
    db_name: str = config('DB_NAME', cast=str)
    db_host: str = config('DB_HOST', cast=str)
    db_port: int = config('DB_PORT', cast=int)

    @property
    def db_config(self) -> str:
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"


@lru_cache
def get_settings():
    return Settings()
