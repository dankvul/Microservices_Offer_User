from sanic import Blueprint
from sanic.response import json

from controller.decorators import json_is_valid, catch_exceptions, authorized
from controller.schemas import signup_schema, login_schema
from database.crud import UserCRUD


bp = Blueprint('user', url_prefix="/user")


@bp.route("/registry/", methods=["POST"])
@catch_exceptions
@json_is_valid(signup_schema)
async def signup(request):
    await UserCRUD.create_safe(user_data=request.json)
    return json({"status": "success"}, 201)


@bp.route("/auth/", methods=["POST"])
@catch_exceptions
@json_is_valid(login_schema)
async def login(request):
    login_response = await UserCRUD.login(user_data=request.json)
    return json(login_response)


@bp.route("/<user_id>/", methods=["GET"])
@catch_exceptions
@authorized
async def get_user(request, user_id: str, *args, **kwargs):
    return await UserCRUD.get_user_info(user_id, request.token)
