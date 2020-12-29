from database import db
from database.models import BaseModel


class Offer(BaseModel):
    __tablename__ = "offers"

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    title = db.Column(db.String(length=32))
    text = db.Column(db.String(length=256))

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "title": self.title,
            "text": self.text
        }
