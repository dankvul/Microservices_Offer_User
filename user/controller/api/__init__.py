from sanic import Blueprint

from controller.api.user import bp as user_bp


bp = Blueprint.group(user_bp, url_prefix="/api")
