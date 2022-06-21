from src import db


class User(db.Model):
    userId = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    birth_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
