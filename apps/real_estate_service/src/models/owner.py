from datetime import datetime
from src import db

class Owner(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, auto_increment=False)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    real_estate = db.relationship('RealEstate', backref='owner', lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())