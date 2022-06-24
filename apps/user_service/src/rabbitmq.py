import json
import pika


class RabbitMQ:
    channel = None
    connection = None

    @staticmethod
    def get_connection() -> None:
        credentials = pika.PlainCredentials('user', 'password')
        parameters = pika.ConnectionParameters(
            host='rabbitmq', credentials=credentials)
        RabbitMQ.connection = pika.BlockingConnection(parameters)
        RabbitMQ.channel = RabbitMQ.connection.channel()

    @staticmethod
    def declare_new_channel(channel_name: str) -> None:
        if RabbitMQ.channel is None:
            raise Exception('Cannot create new channel, channel is empty')

        RabbitMQ.channel.queue_declare(queue=channel_name)

    @staticmethod
    def publish_message(channel_name: str, message: dict) -> None:
        if RabbitMQ.channel is None:
            raise Exception('Cannot create new channel, channel is empty')

        RabbitMQ.channel.basic_publish(
            exchange='', routing_key=channel_name, body=json.dumps(message))

        print("[x] Sent %r" % message)

    @staticmethod
    def receive_message_from_queue(queue_name: str, callback) -> None:
        RabbitMQ.channel.basic_consume(queue=queue_name,
                                       auto_ack=True,
                                       on_message_callback=callback)
