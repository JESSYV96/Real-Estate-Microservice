import os
from jwt import decode


def get_payload_from_token(token: str) -> dict:
    return decode(token[7:], os.environ.get('JWT_SECRET'), algorithms="HS256")
