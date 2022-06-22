import pika
import logging


class RabbitMQ:
    channel = None

    @staticmethod
    def get_connection() -> None:
        credentials = pika.PlainCredentials('user', 'password')
        parameters = pika.ConnectionParameters(
            host='rabbitmq', credentials=credentials)
        connection = pika.BlockingConnection(parameters)
        RabbitMQ.channel = connection.channel()
        logging.info(
            '------- Connection to RabbitMQ User service is successful ------')

    @staticmethod
    def create_new_channel(channel_name: str) -> None:
        if RabbitMQ.channel is None:
            raise Exception('Cannot create new channel, channel is empty')

        RabbitMQ.channel.queue_declare(queue=channel_name)

    @staticmethod
    def publish_message(channel_name: str, message):
        if RabbitMQ.channel is None:
            raise Exception('Cannot create new channel, channel is empty')

        RabbitMQ.channel.basic_publish(
            exchange='', routing_key=channel_name, body=message)

    @staticmethod
    def get_message_from_queue():
        pass
