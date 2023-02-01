from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_sample_route():
    response = client.get('/sample_app/sample_route')
    assert response.status_code == 200
    assert response.json() == {'name': 'Hello world'}
