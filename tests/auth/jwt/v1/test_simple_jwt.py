import pytest
from decouple import config
from jose import jwt

from src.auth.jwt.v1.utils import SimpleJWT


@pytest.mark.auth
@pytest.mark.jwt
async def test_initialization_without_params():
    instance = SimpleJWT()

    assert isinstance(instance, SimpleJWT)
    assert instance._JWT_SECRET == config("SECRET_KEY", cast=str)
    assert instance._ALGORITHM == config("JWT_ALGORITHM", cast=str)
    assert instance._ACCESS_TOKEN_LIFETIME == config("JWT_ACCESS_TOKEN_LIFETIME_MINUTES", cast=str)


@pytest.mark.auth
@pytest.mark.jwt
async def test_initialization_with_params():
    secret = "secret"
    algorithm = "algorithm"
    access_token_lifetime = 11

    instance = SimpleJWT(secret, algorithm, access_token_lifetime)

    assert isinstance(instance, SimpleJWT)
    assert instance._JWT_SECRET != config("SECRET_KEY", cast=str)
    assert instance._ALGORITHM != config("JWT_ALGORITHM", cast=str)
    assert instance._ACCESS_TOKEN_LIFETIME != config("JWT_ACCESS_TOKEN_LIFETIME_MINUTES", cast=str)

    assert instance._JWT_SECRET == secret
    assert instance._ALGORITHM == algorithm
    assert instance._ACCESS_TOKEN_LIFETIME == access_token_lifetime


async def test_token_creation():
    simple_jwt = SimpleJWT(secret="secret", algorithm="HS256")
    data = {"user": 12}

    token = simple_jwt.create_access_token(data)
    decoded_data = jwt.decode(
        token=token,
        key='secret',
        algorithms=["HS256"],
    )

    assert isinstance(token, str)
    assert data == {"user": 12}
    assert "user" in decoded_data
    assert "exp" in decoded_data
    assert "iss" in decoded_data
    assert isinstance(decoded_data["user"], int)
    assert isinstance(decoded_data["exp"], int)
    assert isinstance(decoded_data["iss"], str)
