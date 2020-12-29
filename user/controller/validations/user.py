from database.models import User
from utils import pwd_context
from exceptions import (
    EmailAlreadyExistsError,
    UsernameAlreadyExistsError,
    WrongUsernameOrPasswordError,
)


__all__ = ["UserValidations"]


class UserValidations:
    @staticmethod
    async def _check_same_username(username: str) -> None:
        user = await User.query.where(User.username == username).gino.first()
        if user is not None:
            raise UsernameAlreadyExistsError()

    @staticmethod
    async def _check_same_email(email: str) -> None:
        user = await User.query.where(User.email == email).gino.first()
        if user is not None:
            raise EmailAlreadyExistsError()

    @classmethod
    async def signup_validation(cls, email: str, username: str) -> None:
        await cls._check_same_email(email)
        await cls._check_same_username(username)

    @staticmethod
    async def login_validation(username: str, password: str) -> None:
        user = await User.query.where(User.username == username).gino.first()
        if user is None or not pwd_context.verify(password, user.password):
            raise WrongUsernameOrPasswordError()
