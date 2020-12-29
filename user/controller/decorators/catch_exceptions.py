from functools import wraps
from sanic.response import json

from exceptions.user import UserBaseException


__all__ = ["catch_exceptions"]


def catch_exceptions(f):
    @wraps(f)
    async def decorated_function(request, *args, **kwargs):
        try:
            result = await f(request, *args, **kwargs)
        except UserBaseException as error:
            return json({"error": str(error)}, error.http_status.value)
        return result
    return decorated_function
