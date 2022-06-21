import os


from flask import Flask
from src.controllers import real_estate


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
        )
    else:
        app.config.from_mapping(test_config)

    app.register_blueprint(real_estate.real_estate_route)

    return app
