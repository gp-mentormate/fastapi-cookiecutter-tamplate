from uuid import UUID

from pydantic import BaseModel, EmailStr


class BaseUser(BaseModel):
    email: EmailStr


class UserCreateIn(BaseUser):
    password: str


class UserCreateOut(BaseUser):
    id: UUID

    class Config:
        orm_mode = True

