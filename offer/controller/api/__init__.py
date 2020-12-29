from sanic import Blueprint

from controller.api.user import bp as user_bp
from controller.api.offer import bp as offer_bp


bp = Blueprint.group(user_bp, offer_bp, url_prefix="/api")
