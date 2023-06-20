from uuid import UUID

from pydantic import EmailStr
from sqlalchemy import select, insert

from src.users.v1.models import User
from src.utils import DBSessionMixin


class UserCRUD(DBSessionMixin):

    # Create methods
    async def create_user(self, email: EmailStr, password: str):
        stmt = insert(User).values(email=email, password=password)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.inserted_primary_key[0]

    # Retrieve methods
    async def get_all_users(self):
        stmt = select(User)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_user_by_id(self, user_id: UUID):
        statement = select(User).where(User.id == user_id)
        result = await self.session.execute(statement)
        return result.scalars().first()

    async def get_users_by_email(self, email: EmailStr):
        statement = select(User).where(User.email == email)
        result = await self.session.execute(statement)
        return result.scalars().all()

    # Update methods
    # ...

    # Delete methods
    # ...
