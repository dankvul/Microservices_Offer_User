from database.crud import UserCRUD
from exceptions import (
    UserAlreadyExists,
    WrongSecretError
)
from config import SECRET


__all__ = ["UserValidations"]


class UserValidations:
    @staticmethod
    async def add_user_validation(user_id: int, secret: str) -> None:
        if await UserCRUD.find_by_id(user_id):
            raise UserAlreadyExists()
        if secret != SECRET:
            raise WrongSecretError()
