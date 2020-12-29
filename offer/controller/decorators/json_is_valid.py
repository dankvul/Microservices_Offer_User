from functools import wraps

from controller.schemas import SchemaValidator
from exceptions import SchemaValidationError


__all__ = ["json_is_valid"]


def json_is_valid(schema: dict):
    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            error_msg = await SchemaValidator(schema).validate_json(request.json)
            if error_msg:
                raise SchemaValidationError(msg=error_msg)
            else:
                return await f(request, *args, **kwargs)
        return decorated_function
    return decorator
