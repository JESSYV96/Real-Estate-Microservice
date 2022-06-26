from functools import wraps
from flask import request

from src.models.real_estate import RealEstate
from src.helpers.jwt import get_payload_from_token


def real_estate_owner(func):
    @wraps(func)
    def is_real_estate_owner(*args, **kwargs) -> bool:
        token = request.headers.get('Authorization')

        if token is None:
            raise Exception('Token not found')

        current_owner = get_payload_from_token(token)

        owner_real_estate_id = RealEstate.query.get(
            kwargs['real_estate_id']).owner_id

        owner_id = current_owner['user_id']

        if owner_id is not owner_real_estate_id:
            raise PermissionError(
                "You not allowed to edit this property, you are not the owner")

        result = func(*args, **kwargs)

        return result

    return is_real_estate_owner
