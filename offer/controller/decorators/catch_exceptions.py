from functools import wraps
from sanic.response import json

from exceptions import BaseExceptionClass


__all__ = ["catch_exceptions"]


def catch_exceptions(f):
    @wraps(f)
    async def decorated_function(request, *args, **kwargs):
        try:
            result = await f(request, *args, **kwargs)
        except BaseExceptionClass as error:
            return json({"error": str(error)}, error.http_status.value)
        return result
    return decorated_function
