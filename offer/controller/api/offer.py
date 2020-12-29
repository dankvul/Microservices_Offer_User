from sanic import Blueprint
from sanic.response import json

from database.crud import OfferCRUD
from controller.decorators import json_is_valid, catch_exceptions, authorized
from controller.schemas import create_offer_schema, get_offer_schema
from controller.validations import OfferValidations


bp = Blueprint('offer', url_prefix="/offer")


@bp.route("/create/", methods=["POST"])
@catch_exceptions
@json_is_valid(create_offer_schema)
@authorized
async def create_offer(request, *args, **kwargs):
    offer_data = request.json
    await OfferValidations.user_id_validation(offer_data.get("user_id"))
    await OfferCRUD.add_offer(offer_data)
    return json({"status": "success"}, 201)


@bp.route("/", methods=["POST"])
@catch_exceptions
@json_is_valid(get_offer_schema)
@authorized
async def get_offers(request, *args, **kwargs):
    offer_get_data = request.json
    if offer_get_data.get("user_id"):
        await OfferValidations.user_id_validation(offer_get_data.get("user_id"))
    return await OfferCRUD.get_offers_info(offer_data=offer_get_data)

