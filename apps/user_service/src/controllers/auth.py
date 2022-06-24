
from datetime import datetime
from flask import Blueprint, request

from src.models.user import User
from src.helpers.hash import generate_hash, verify_hash
from src.helpers.jwt import generate_token
from src.repositories.user import add_user

auth_blueprint = Blueprint('auth', __name__, url_prefix='/api/v1/auth')


@auth_blueprint.post('/register')
def register():
    new_user_email = request.json['email']
    new_user_password = request.json['password']

    if User.query.filter_by(email=new_user_email).first() is not None:
        raise Exception('This email is already used')

    password_hashed = generate_hash(new_user_password)

    new_user = User(
        firstname=request.json['firstname'],
        lastname=request.json['lastname'],
        birth_date=datetime.strptime(
            request.json['birth_date'], '%d/%m/%Y').date(),
        email=new_user_email,
        password=password_hashed)

    add_user(new_user)

    # RabbitMQ.publish_message("user_created", {"user_id": new_user.userId})

    return f'{new_user.userId}'


@auth_blueprint.post('/login')
def login() -> str:
    email = request.json['email']
    password = request.json['password']

    user = User.query.filter_by(email=email).first()

    if user is None:
        raise Exception('Login error')

    if verify_hash(word_to_check=password, word_hashed=user.password) is False:
        raise Exception('Login error')

    return generate_token()


@auth_blueprint.post('/logout')
def logout() -> str:
    return 'User Logout'
