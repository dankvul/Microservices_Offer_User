from typing import Optional, List
from sanic.response import json


from database.models import Offer, User
from database import db


class OfferCRUD:
    @staticmethod
    async def find_by_id(_id: int) -> Optional[Offer]:
        return await Offer.get(_id)

    @staticmethod
    async def add_offer(offer_data: dict) -> None:
        await Offer.create(
            user_id=offer_data.get("user_id"),
            title=offer_data.get("title"),
            text=offer_data.get("text"),
        )

    @staticmethod
    async def get_offers_by_user_id(user_id: int) -> List[Offer]:
        user = await OfferCRUD.find_by_id(user_id)
        offers = await Offer.query.where(Offer.user_id == user.id).gino.all()

        return offers

    @staticmethod
    async def get_offers_info(offer_data: dict) -> dict:
        if offer_data.get("user_id"):
            offers = await OfferCRUD.get_offers_by_user_id(offer_data.get("user_id"))
            offers = list(map(lambda offer: offer.serialize(), offers))
            return json({
                "offers": offers
            }, 200)
        elif offer_data.get("offer_id"):
            return json({
                "offers": (await OfferCRUD.find_by_id(offer_data.get("offer_id"))).serialize()
            }, 200)

