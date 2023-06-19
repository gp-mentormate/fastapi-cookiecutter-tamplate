from uuid import UUID

from pydantic import EmailStr
from sqlalchemy import select, insert

from src.database import session
from src.users.v1.models import User


class UserCRUD:

    # Create methods
    @staticmethod
    async def create_user(email: EmailStr, password: str):
        async with session() as db:
            stmt = insert(User).values(email=email, password=password)
            await db.execute(stmt)
            result = await db.commit()
            return result

    # Retrieve methods
    @staticmethod
    async def get_all_users():
        async with session() as db:
            stmt = select(User)
            result = await db.execute(stmt)
            return result.scalars().all()

    @staticmethod
    async def get_user_by_id(user_id: UUID):
        async with session() as db:
            statement = select(User).where(User.id == user_id)
            result = await db.execute(statement)
            return result.scalars().all()

    @staticmethod
    async def get_users_by_email(email: EmailStr):
        async with session() as db:
            statement = select(User).where(User.email == email)
            result = await db.execute(statement)
            return result.scalars().all()

    # Update methods
    # ...

    # Delete methods
    # ...
