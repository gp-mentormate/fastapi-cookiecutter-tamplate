import uuid

from sqlalchemy import Column, String

from src.database import Base
from src.utils import GUID


class User(Base):
    __tablename__ = 'users'

    id = Column(
        GUID(), primary_key=True, default=uuid.uuid4, unique=True
    )
    email = Column(String(100), unique=True)
    password = Column(String(100))
