import asyncio
import json
import os
from typing import Generator

import pytest
import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from src.database import async_engine, Base
from src.main import app


@pytest.fixture(scope="session")
def event_loop(request) -> Generator:  # noqa: indirect usage
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture
async def async_client():
    async with AsyncClient(
            app=app,
            base_url=f"http://localhost"
    ) as client:
        yield client


@pytest_asyncio.fixture(scope="function")
async def async_session() -> AsyncSession:
    session = sessionmaker(
        async_engine, class_=AsyncSession, expire_on_commit=False
    )

    async with session() as s:
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        yield s

    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

    await async_engine.dispose()
