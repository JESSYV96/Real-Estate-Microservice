from flask import Blueprint

real_estate_route = Blueprint('real_estate', __name__, url_prefix='/api/v1/real_estate')


@real_estate_route.get('/')
def get_real_estate_by_city() -> str:
    return 'List of real estate'