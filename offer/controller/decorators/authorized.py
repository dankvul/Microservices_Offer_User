from functools import wraps

from database.crud import UserCRUD
from exceptions import UnauthorizedError
from utils import JWT


__all__ = ["authorized"]


def authorized(f):
    @wraps(f)
    async def decorated_function(request, *args, **kwargs):
        token = request.token
        if token is not None:
            decoded_token = JWT.decode_jwt_token(token)
            if decoded_token is not None:
                auth_user = await UserCRUD.find_by_id(decoded_token.get("user_id"))
                if auth_user:
                    kwargs["user"] = auth_user
                    return await f(request, *args, **kwargs)
        raise UnauthorizedError()

    return decorated_function
