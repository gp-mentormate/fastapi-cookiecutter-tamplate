from uuid import UUID

from fastapi import HTTPException
from pydantic import EmailStr
from sqlalchemy.exc import SQLAlchemyError
from starlette import status

from src.logger import logger
from src.users.v1.crud import UserCRUD
from src.users.v1.models import User


class UserService:

    @staticmethod
    async def create_new_user(email: EmailStr, password: str):
        # Insert the user in the database
        try:
            user_id: UUID = await UserCRUD.create_user(email, password)
        except SQLAlchemyError as e:
            logger.error(e)

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The user is not created!"
            )

        logger.info(f"User with id {user_id} was created successfully.")

        # Fetch the new row from the database
        try:
            user: User = await UserCRUD.get_user_by_id(user_id)
        except SQLAlchemyError as e:
            logger.error(e)

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Something went wrong but the user is created!"
            )

        # Sent email for the successful registration to the user
        # ...

        # Sent emails for the successful registration to the site admins
        # ...

        return user
