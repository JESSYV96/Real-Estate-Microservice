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
        print('------- Connection to RabbitMQ Real estate service is successful ------')

    @staticmethod
    def create_new_channel(channel_name: str) -> None:
        if RabbitMQ.channel is None:
            raise Exception('Cannot create new channel, channel is empty')

        RabbitMQ.channel.queue_declare(queue=channel_name)
