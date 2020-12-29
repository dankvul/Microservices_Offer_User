from typing import Optional

from database.models import User


class UserCRUD:
    @staticmethod
    async def find_by_id(user_id: int) -> Optional[User]:
        return await User.get(user_id)

    @staticmethod
    async def add_user(user_data: dict) -> None:
        await User.create(
            id=user_data.get("user_id"),
            username=user_data.get("username")
        )
