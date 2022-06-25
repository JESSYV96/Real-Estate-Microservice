from datetime import datetime
from flask import Blueprint, request

from src.models.user import User
from src.database import db

users_blueprint = Blueprint('users', __name__, url_prefix='/api/v1/users')


@users_blueprint.put('/<user_id>')
def edit_user_info(user_id) -> User:
    user = User.query.get(user_id)

    if user is None:
        raise Exception('User not found')

    user.firstname = request.json['firstname'] or user.firstname
    user.lastname = request.json['lastname'] or user.lastname
    user.email = request.json['email'] or user.email
    user.birth_date = datetime.strptime(
        request.json['birth_date'], '%d/%m/%Y').date() or user.birth_date

    db.session.commit()

    return user.to_JSON()
