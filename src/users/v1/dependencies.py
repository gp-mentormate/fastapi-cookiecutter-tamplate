from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.users.v1.crud import UserCRUD
from src.users.v1.service import UserService


async def get_users_crud(
        session: AsyncSession = Depends(get_async_session)
) -> UserCRUD:
    return UserCRUD(session=session)


async def get_users_service(
        session: AsyncSession = Depends(get_async_session)
) -> UserService:
    return UserService(session=session)
