import os


from flask import Flask
from src.models.rabbitmq import RabbitMQ
from src.database import db
from src.controllers import auth, users


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI='mariadb+pymysql://user:root@arcane_user_db/user_db?charset=utf8mb4',
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
        )
    else:
        app.config.from_mapping(test_config)

    app.register_blueprint(auth.auth_blueprint)
    app.register_blueprint(users.users_blueprint)

    db.app = app
    db.init_app(app)

    RabbitMQ.get_connection()
    RabbitMQ.create_new_channel('test')
    RabbitMQ.create_new_channel('hello')

    return app
