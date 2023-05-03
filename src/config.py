from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    db_host: str
    db_user: str
    db_password: str
    db_name: str
    @property
    def db_config(self) -> str:
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}/{self.db_name}"

    # # JWT auth related variables.
    # jwt_sig_kid: str
    # jwt_public_key: str
    # jwt_private_key: str
    # jwt_algorithm: str
    # access_token_expiration: int
    # refresh_token_expiration: int

    # # AWS config
    # aws_access_key: str
    # aws_secret_key: str
    # aws_region: str


@lru_cache
def get_settings():
    return Settings()
