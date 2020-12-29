from abc import ABC
from typing import Optional
from http import HTTPStatus


__all__ = [
    "UserBaseException",
    "UnauthorizedError",
    "EmailAlreadyExistsError",
    "UsernameAlreadyExistsError",
    "WrongUsernameOrPasswordError",
    "SchemaValidationError",
    "InvalidParameters"
]


class UserBaseException(Exception, ABC):
    http_status: HTTPStatus = None
    base_message: Optional[str] = None

    def __init__(self, msg: Optional[str] = None) -> None:
        super().__init__(self.base_message if msg is None else msg)


class UnauthorizedError(UserBaseException):
    http_status = HTTPStatus.UNAUTHORIZED
    base_message = "Unauthorized"


class EmailAlreadyExistsError(UserBaseException):
    http_status = HTTPStatus.BAD_REQUEST
    base_message = "Email already exists"


class UsernameAlreadyExistsError(UserBaseException):
    http_status = HTTPStatus.BAD_REQUEST
    base_message = "Username already exists"


class WrongUsernameOrPasswordError(UserBaseException):
    http_status = HTTPStatus.BAD_REQUEST
    base_message = "Wrong username or password"


class SchemaValidationError(UserBaseException):
    http_status = HTTPStatus.BAD_REQUEST
    base_message = "Json validation error"


class InvalidParameters(UserBaseException):
    http_status = HTTPStatus.BAD_REQUEST
    base_message = "Invalid parameter(s)"
