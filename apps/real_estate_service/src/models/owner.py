from datetime import datetime

from src.database import db


class Owner(db.Model):
    __tablename__ = 'owners'

    owner_id = db.Column(db.Integer, primary_key=True)
    real_estate = db.relationship(
        'RealEstate', backref='real_estate', lazy=True)

    def __repr__(self):
        return '<Owner %r>' % self.owner_id
