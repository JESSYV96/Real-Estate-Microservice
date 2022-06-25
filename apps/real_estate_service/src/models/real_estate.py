from datetime import datetime
from enum import Enum

from src.database import db

# Maybe use a Literal instead of Enum
class KindRealEstate(Enum):
    APPARTMENT = 'appartment'
    HOUSE = 'house'


# class Room(object):
#     slug = db.Column(db.String(100), nullable=False,
#                      unique=True, primary_key=True)
#     pretty_name = db.Column(db.String(100), nullable=False)


class RealEstate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    kind = db.Column(db.Enum(KindRealEstate), nullable=False)
    description = db.Column(db.Text())
    city = db.Column(db.String(100), nullable=False)
    surface = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(
        db.DateTime,  default=datetime.now(), onupdate=datetime.now())
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'))

    def to_JSON(self):
        return {
            "id": self.id,
            "owner_id": self.owner_id,
            "name": self.name,
            "kind": self.kind.value,
            "description": self.description,
            "city": self.city,
            "surface": self.surface,
            "created_at": self.date_to_str(self.created_at),
            "updated_at": self.date_to_str(self.updated_at)
        }

    def date_to_str(self, date):
        return date.strftime('%d/%m/%Y')

    def __repr__(self):
        return '<RealEstate %r>' % self.name
