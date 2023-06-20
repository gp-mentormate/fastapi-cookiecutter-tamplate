from typing import Optional, List
from uuid import UUID

from fastapi import APIRouter

from src.users.v1.crud import UserCRUD
from src.users.v1.schemas import UserCreateIn, UserCreateOut
from src.users.v1.service import UserService

router = APIRouter(
    prefix="/api/v1/users",
    tags=["users"]
)


@router.get("/", response_model=List[UserCreateOut])
async def get_users(user_id: Optional[UUID] = None):
    if user_id:
        return [await UserCRUD.get_user_by_id(user_id)]

    return await UserCRUD.get_all_users()


@router.post("/", response_model=UserCreateOut)
async def create_user(user_data: UserCreateIn):
    return await UserService.create_new_user(**user_data.dict())
