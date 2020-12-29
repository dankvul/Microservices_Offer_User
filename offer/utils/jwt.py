import jwt
from jwt import DecodeError, ExpiredSignatureError
from datetime import datetime, timedelta

from config import EXPIRES_DELTA, ALGORITHM, SECRET


__all__ = ["JWT"]


class JWT:
    @staticmethod
    def encode_jwt_token(data: dict, expire_delta: timedelta = None) -> str:
        to_encode = data.copy()

        if expire_delta:
            expire = datetime.utcnow() + expire_delta
        elif EXPIRES_DELTA:
            expire = datetime.utcnow() + EXPIRES_DELTA
        else:
            expire = None

        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, SECRET, algorithm=ALGORITHM).decode("UTF-8")

    @staticmethod
    def decode_jwt_token(token: str):
        data = None

        try:
            data = jwt.decode(token, SECRET, verify=True, algorithms=ALGORITHM)

            if data.get("exp") and datetime.fromtimestamp(data.get("exp")) < datetime.now():
                data = None

        except (DecodeError, ExpiredSignatureError):
            pass

        return data
