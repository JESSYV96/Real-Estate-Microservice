from datetime import datetime
from enum import Enum

from src.database import db

# Maybe use a Literal instead of Enum


class KindRealEstate(Enum):
    APPARTMENT = 'appartment'
    HOUSE = 'house'


class RealEstate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    kind = db.Column(db.Enum(KindRealEstate), nullable=False)
    description = db.Column(db.Text())
    city = db.Column(db.String(100), nullable=False)
    surface = db.Column(db.Integer, nullable=False)  # en m2
    is_furnished = db.Column(db.Boolean, nullable=False)
    rooms = db.relationship(
        'Room', lazy=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(
        db.DateTime,  default=datetime.now(), onupdate=datetime.now())

    def to_JSON(self):
        return {
            "id": self.id,
            "owner_id": self.owner_id,
            "name": self.name,
            "kind": self.kind.value,
            "description": self.description,
            "city": self.city,
            "surface": self.surface,
            "is_furnished": self.is_furnished,
            "created_at": self.date_to_str(self.created_at),
            "updated_at": self.date_to_str(self.updated_at)
        }

    def date_to_str(self, date):
        return date.strftime('%d/%m/%Y')

    def __repr__(self):
        return '<RealEstate %r>' % self.name
