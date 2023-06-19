from uuid import UUID

from pydantic import EmailStr
from sqlalchemy.exc import SQLAlchemyError

from src.logger import logger
from src.security import get_password_hash
from src.users.v1.crud import UserCRUD
from src.users.v1.exceptions import (
    UserNotCreatedException,
    SomethingWentWrongException
)
from src.users.v1.models import User


class UserService:

    @staticmethod
    async def create_new_user(email: EmailStr, password: str):
        # Secure the user password
        password_hash: str = get_password_hash(password)

        # Insert the user in the database
        try:
            user_id: UUID = await UserCRUD.create_user(email, password_hash)
        except SQLAlchemyError as e:
            logger.error(e)

            raise UserNotCreatedException()

        logger.info(f"User with id {user_id} was created successfully.")

        # Fetch the new row from the database
        try:
            user: User = await UserCRUD.get_user_by_id(user_id)
        except SQLAlchemyError as e:
            logger.error(e)

            raise SomethingWentWrongException()

        # Sent email for the successful registration to the user
        # ...

        # Sent emails for the successful registration to the site admins
        # ...

        return user
