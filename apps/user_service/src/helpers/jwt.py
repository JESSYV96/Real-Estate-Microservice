import os
from jwt import encode


def generate_token(payload: dict) -> str:
    return encode(payload, os.environ.get("JWT_SECRET"), algorithm="HS256")


def verify_token(token: str):
    pass
