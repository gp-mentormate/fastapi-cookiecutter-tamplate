from fastapi import HTTPException
from fastapi import status


class UserNotCreatedException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The user is not created!"
        )


class SomethingWentWrongException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong!"
        )
