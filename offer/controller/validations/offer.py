from database.crud import UserCRUD
from exceptions import (
    NoSuchUserError
)

__all__ = ["OfferValidations"]


class OfferValidations:
    @staticmethod
    async def user_id_validation(user_id: int) -> None:
        if not await UserCRUD.find_by_id(user_id):
            raise NoSuchUserError()
