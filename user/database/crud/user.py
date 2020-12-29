from typing import Optional, Union
from sanic.response import json

from database.models import User
from controller.validations import UserValidations
from utils import JWT, pwd_context, Requests
from exceptions.user import InvalidParameters


class UserCRUD:
    @staticmethod
    async def find_by_id(user_id: int) -> Optional[User]:
        return await User.get(user_id)

    @classmethod
    async def create_safe(cls, user_data: dict) -> None:
        await UserValidations.signup_validation(
                email=user_data.get("email"),
                username=user_data.get("username")
        )
        user = await User.create(
            username=user_data.get("username"),
            email=user_data.get("email"),
            password=pwd_context.hash(user_data.get("password")),
        )
        await Requests.send_new_user_request(user_id=user.id, username=user.username)
        # TODO: Do smth when offer is down

    @classmethod
    async def login(cls, user_data: dict) -> dict:
        await UserValidations.login_validation(
            username=user_data.get("username"),
            password=user_data.get("password"),
        )

        user = await User.query.where(User.username == user_data.get("username")).gino.first()

        token = JWT.encode_jwt_token({"user_id": user.id})

        return {
            "token": token,
            "user_id": user.id
        }

    @classmethod
    async def get_user_info(cls, user_id: str, token: str):
        if not user_id.isdigit():
            raise InvalidParameters()
        target_user = await cls.find_by_id(int(user_id))
        return json({
            "user": target_user.serialize() if target_user else None,
            **(await Requests.get_offers_by_user_id(int(user_id), token))
        }, 200)
