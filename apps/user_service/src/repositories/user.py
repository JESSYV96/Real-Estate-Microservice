from src.database import db
from src.models.user import User


def add_user(new_user: User):
    db.session.add(new_user)
    db.session.commit()
