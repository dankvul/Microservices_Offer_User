from http import HTTPStatus

from .base import BaseExceptionClass


__all__ = [
    "UserAlreadyExists",
    "UnauthorizedError",
    "WrongSecretError",
    "NoSuchUserError",
]


class UserAlreadyExists(BaseExceptionClass):
    http_status = HTTPStatus.BAD_REQUEST
    base_message = "User already fetched"


class WrongSecretError(BaseExceptionClass):
    http_status = HTTPStatus.UNAUTHORIZED
    base_message = "Wrong secret"


class UnauthorizedError(BaseExceptionClass):
    http_status = HTTPStatus.UNAUTHORIZED
    base_message = "Unauthorized"


class NoSuchUserError(BaseExceptionClass):
    http_status = HTTPStatus.BAD_REQUEST
    base_message = "No such user"
