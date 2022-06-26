from enum import Enum, unique

from src.database import db


@unique
class KindRoom(Enum):
    LIVING_ROOM = 'living_room'
    BEDROOM = 'bedroom'
    BALCONY = 'balcony'
    SHOWER = 'shower'
    KITCHEN = 'kitchen'


class Room(db.Model):
    __tablename__ = 'rooms'

    id = db.Column(db.Integer, primary_key=True)
    kind = db.Column(db.Enum(KindRoom), nullable=False)
    real_estate_id = db.Column(db.Integer, db.ForeignKey('real_estate.id'))

    def to_JSON(self):
        return {
            "id": self.id,
            "kind": self.kind.value,
            "real_estate_id": self.real_estate_id
        }
