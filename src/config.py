from functools import lru_cache

from decouple import config
from pydantic import BaseSettings, conint, RedisDsn


class DatabaseSettings(BaseSettings):
    db_user: str = config('DB_USER', cast=str)
    db_password: str = config('DB_PASSWORD', cast=str)
    db_name: str = config('DB_NAME', cast=str)
    db_host: str = config('DB_HOST', cast=str)
    db_port: conint(ge=1, le=65535) = config('DB_PORT', cast=int)

    @property
    def db_connection_url(self) -> str:
        if config("FASTAPI_TEST", cast=bool, default=False):
            return "sqlite+aiosqlite:///:memory:"
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"


class CacheSettings(BaseSettings):
    cache_host: str = config('CACHE_HOST', cast=str)
    cache_port: conint(ge=1, le=65535) = config('CACHE_PORT', cast=int)
    cache_password: str = config('CACHE_PASSWORD', cast=str)
    cache_db_index: int = config('CACHE_DB_INDEX', cast=int)

    @property
    def cache_connection_url(self) -> RedisDsn:
        return RedisDsn(
            f"redis://{self.cache_host}:{self.cache_port}/{self.cache_db_index}"
        )


class JWTSettings(BaseSettings):
    secret = config("SECRET_KEY", cast=str)
    algorithm = config("JWT_ALGORITHM", cast=str)
    life_time = config("JWT_ACCESS_TOKEN_LIFETIME_MINUTES", cast=str)


class Settings(
    DatabaseSettings,
    CacheSettings,
    JWTSettings
):
    debug_mode: bool = config("DEBUG", cast=bool, default=False)


@lru_cache
def get_settings():
    return Settings()
