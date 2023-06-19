from sqlalchemy.ext.asyncio import create_async_engine, \
    async_sessionmaker
from sqlalchemy.orm import declarative_base

from .config import DatabaseSettings

Base = declarative_base()

settings = DatabaseSettings()

async_engine = create_async_engine(
    settings.db_connection_url, future=True
)

session = async_sessionmaker(async_engine)


async def get_async_db():
    db = session()
    try:
        yield db
    finally:
        await db.close()
