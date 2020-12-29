from sanic import Blueprint
from sanic.response import json

from database.crud import UserCRUD
from controller.decorators import json_is_valid, catch_exceptions, authorized
from controller.schemas import add_user_schema
from controller.validations import UserValidations


bp = Blueprint('user', url_prefix="/user")


@bp.route("/", methods=["POST"])
@catch_exceptions
@json_is_valid(add_user_schema)
async def add_user(request):
    user_data = request.json
    await UserValidations.add_user_validation(user_data.get("user_id"), user_data.get("secret"))
    await UserCRUD.add_user(user_data)
    return json({"status": "success"}, 201)
