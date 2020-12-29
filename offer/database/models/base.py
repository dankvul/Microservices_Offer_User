from database import db


class BaseModel(db.Model):
    __abstract__ = True

    def add_to_db(self) -> None:
        db.session.add(self)
        db.session.commit(self)
