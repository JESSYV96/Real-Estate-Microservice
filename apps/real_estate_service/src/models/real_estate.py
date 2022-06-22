from datetime import datetime
from src import db


class RealEstate(db.Model):
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text())
    city = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.user_id'))
