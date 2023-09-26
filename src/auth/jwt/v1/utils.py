import socket
from datetime import timedelta, datetime
from typing import Optional

from decouple import config
from jose import jwt

from src.config import JWTSettings


class SimpleJWT:
    _JWT_SECRET = None
    _ALGORITHM = None
    _ACCESS_TOKEN_LIFETIME = None

    def __init__(
            self,
            secret: Optional[str] = None,
            algorithm: Optional[str] = None,
            access_token_lifetime: Optional[int] = None
    ):
        jwt_default_settings = JWTSettings()

        self._JWT_SECRET = secret if secret else jwt_default_settings.secret
        self._ALGORITHM = algorithm if algorithm else jwt_default_settings.algorithm
        self._ACCESS_TOKEN_LIFETIME = access_token_lifetime if access_token_lifetime else jwt_default_settings.life_time

    def create_access_token(self, data: dict) -> str:
        hostname = socket.gethostname()

        to_encode = data.copy()
        expire = datetime.utcnow()
        to_encode.update({"iss": hostname, "exp": expire})
        encoded_jwt = jwt.encode(to_encode, self._JWT_SECRET, algorithm=self._ALGORITHM)

        return encoded_jwt

    def validate_token(self, token: Optional[str] = None):
        pass
