from flask import Blueprint


owner_route = Blueprint(
    'owner', __name__, url_prefix='/api/v1/owner')
