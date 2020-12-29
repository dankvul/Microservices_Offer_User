from database import db
from database.models import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True, index=True)
    username = db.Column(db.String(length=128), unique=True, index=True)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username
        }
