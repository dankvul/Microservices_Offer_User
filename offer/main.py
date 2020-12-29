from sanic import Sanic

from database import db_instance
from controller.api import bp

app = Sanic(
    "offer microservice"
)


@app.listener('before_server_start')
async def init_db(app_, loop):
    await db_instance.init()

app.blueprint(bp)
