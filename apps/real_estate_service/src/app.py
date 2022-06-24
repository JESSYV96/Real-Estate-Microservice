import os


from flask import Flask
from src.controllers import owner, real_estate
from src.database import db


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI='sqlite:///real_estate_service.db',
            SQLALCHEMY_TRACK_MODIFICATIONS=True,
        )
    else:
        app.config.from_mapping(test_config)

    db.app = app
    db.init_app(app)
    db.create_all()

    app.register_blueprint(real_estate.real_estate_route)
    app.register_blueprint(owner.owner_route)

    # RabbitMQ.get_connection()
    # RabbitMQ.declare_new_channel('user_created')

    # def callback(ch, method, properties, body):
    #     print("[x] Received %r" % ch)

    # RabbitMQ.receive_message_from_queue(
    #     'user_created', callback)

    # print(' [*] Waiting for messages. To exit press CTRL+C')
    # RabbitMQ.channel.start_consuming()

    return app
