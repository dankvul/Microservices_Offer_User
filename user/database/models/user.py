from database import db
from database.models import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True, index=True)
    email = db.Column(db.String(), unique=True)
    username = db.Column(db.String(length=128), unique=True, index=True)
    password = db.Column(db.String(length=72))

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "password": self.password
        }