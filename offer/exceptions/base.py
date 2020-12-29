from abc import ABC
from typing import Optional
from http import HTTPStatus

__all__ = ["BaseExceptionClass", "SchemaValidationError"]


class BaseExceptionClass(Exception, ABC):
    http_status: HTTPStatus = None
    base_message: Optional[str] = None

    def __init__(self, msg: Optional[str] = None) -> None:
        super().__init__(self.base_message if msg is None else msg)


class SchemaValidationError(BaseExceptionClass):
    http_status = HTTPStatus.BAD_REQUEST
    base_message = "Json validation error"
