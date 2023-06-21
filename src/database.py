from sqlalchemy.ext.asyncio import create_async_engine, \
    async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base

from .config import Settings

Base = declarative_base()

settings = Settings()

async_engine = create_async_engine(
    settings.db_connection_url, future=True, echo=settings.debug_mode
)

async_session = async_sessionmaker(async_engine)


async def get_async_session() -> AsyncSession:
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()
