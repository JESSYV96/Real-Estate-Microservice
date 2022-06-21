from flask import Blueprint, request

from src.models.user import User
from src.helpers.hash import generate_hash
from src.repositories.user import add_user

auth_blueprint = Blueprint('auth', __name__, url_prefix='/api/v1/auth')


@auth_blueprint.post('/register')
def register() -> User:
    new_user_email = request.json['email']
    new_user_password = request.json['password']

    if User.query.filter_by(email=new_user_email).first() is not None:
        raise Exception('This email is already used')

    password_hashed = generate_hash(new_user_password)

    new_user = User(
        firstname=request.json['firstname'],
        lastname=request.json['lastname'],
        email=new_user_email,
        password=password_hashed)

    add_user(new_user)

    return new_user


@auth_blueprint.post('/login')
def login() -> str:
    return 'User Logged'


@auth_blueprint.post('/logout')
def logout() -> str:
    return 'User Logout'
