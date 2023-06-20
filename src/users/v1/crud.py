from uuid import UUID

from pydantic import EmailStr
from sqlalchemy import select, insert

from src.database import async_session
from src.users.v1.models import User


class UserCRUD:

    # Create methods
    @staticmethod
    async def create_user(email: EmailStr, password: str):
        async with async_session() as db:
            stmt = insert(User).values(email=email, password=password)
            result = await db.execute(stmt)
            await db.commit()
            return result.inserted_primary_key[0]

    # Retrieve methods
    @staticmethod
    async def get_all_users():
        async with async_session() as db:
            stmt = select(User)
            result = await db.execute(stmt)
            return result.scalars().all()

    @staticmethod
    async def get_user_by_id(user_id: UUID):
        async with async_session() as db:
            statement = select(User).where(User.id == user_id)
            result = await db.execute(statement)
            return result.scalars().first()

    @staticmethod
    async def get_users_by_email(email: EmailStr):
        async with async_session() as db:
            statement = select(User).where(User.email == email)
            result = await db.execute(statement)
            return result.scalars().all()

    # Update methods
    # ...

    # Delete methods
    # ...
