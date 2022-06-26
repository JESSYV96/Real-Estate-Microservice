from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

db.Table(
    'owners',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('firstname', db.String),
    db.Column('lastname', db.String),
    db.Column('email', db.String)
)
