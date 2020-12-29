import httpx

from config import (
    OFFER_LOCATION,
    OFFER_NEW_USER_METHOD,
    OFFER_GET_OFFERS_METHOD,
    SECRET,
)


__all__ = ["Requests"]


class Requests:
    @staticmethod
    async def send_new_user_request(user_id: int, username: str):
        async with httpx.AsyncClient() as client:
            _ = await client.post(
                headers={"content-type": "application/json"},
                url=f"{OFFER_LOCATION}{OFFER_NEW_USER_METHOD}",
                json={
                    "user_id": user_id,
                    "username": username,
                    "secret": SECRET
                }
            )

    @staticmethod
    async def get_offers_by_user_id(user_id: int, token: str) -> dict:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                headers={
                    "content-type": "application/json",
                    "authorization": f"Bearer {token}"
                },
                url=f"{OFFER_LOCATION}{OFFER_GET_OFFERS_METHOD}",
                json={
                    "user_id": user_id
                },
            )
            return response.json()
