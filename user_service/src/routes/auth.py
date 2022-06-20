from flask import Blueprint, request

auth = Blueprint('auth', __name__, url_prefix='/api/v1/auth')


@auth.post('/register')
def register() -> str:
    print(request.json)
    return 'User Created'


@auth.post('/login')
def login() -> str:
    return 'User Logged'


@auth.post('/logout')
def logout() -> str:
    return 'User Logout'
