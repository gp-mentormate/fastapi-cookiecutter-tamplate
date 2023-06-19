from pydantic import EmailStr

from src.users.v1.crud import UserCRUD


class UserService:

    @staticmethod
    async def create_new_user(email: EmailStr, password: str):
        # Insert the user in the database
        user = await UserCRUD.create_user(email, password)

        # Sent email for the successful registration to the user
        # ...

        # Sent emails for the successful registration to the site admins
        # ...

        return user
