import pytest
from httpx import AsyncClient

from src.main import app


@pytest.mark.asyncio
async def test_registration_success():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/v1/auth/users")
    assert response.status_code == 200
    assert response.json() == {"message": "Tomato"}
