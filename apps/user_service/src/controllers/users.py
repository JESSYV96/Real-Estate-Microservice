from flask import Blueprint

users_blueprint = Blueprint('users', __name__, url_prefix='/api/v1/users')


@users_blueprint.patch('/<user_id>')
def edit_user_data(user_id) -> str:
    return f'User {str(user_id)} edited successfully'
