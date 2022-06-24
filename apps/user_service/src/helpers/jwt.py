import os
from jwt import encode


def generate_token() -> str:
    return encode({"hello": "world"}, os.environ.get("SECRET_KEY"), algorithm="HS256")


def verify_token(token: str):
    pass
