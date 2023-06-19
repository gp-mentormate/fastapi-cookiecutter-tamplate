import databases
from decouple import config
from sqlalchemy.orm import declarative_base

from .config import DatabaseSettings

Base = declarative_base()

settings = DatabaseSettings()

db = databases.Database(
    settings.db_connection_url,
    force_rollback=config("FASTAPI_TEST", cast=bool, default=False)
)
