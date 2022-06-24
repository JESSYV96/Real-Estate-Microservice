from datetime import datetime

from src.database import db


class User(db.Model):
    userId = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    birth_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def to_JSON(self):
        return {
            "userId": self.userId,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "password": self.password,
            "birth_date": self.birth_date,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    def __repr__(self):
        return '<User %r>' % self.email
