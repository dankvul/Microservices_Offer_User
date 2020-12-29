import asyncio

from gino import Gino
from config import DATABASE_URL


class PostgreSQL:
    def __init__(self) -> None:
        self._db = Gino()

    @property
    def db(self) -> Gino:
        return self._db

    async def init(self) -> None:
        await self._db.set_bind(DATABASE_URL)
        await self._db.gino.create_all()


db_instance = PostgreSQL()
db = db_instance.db
