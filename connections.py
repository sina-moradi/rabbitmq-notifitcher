import time
from pika import PlainCredentials, ConnectionParameters, BlockingConnection, exceptions


class RabbitMqConnection:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, host="localhost", port=5672,username="admin",password="admin"):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.connection = None

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def connect(self):
        try:
            credential = PlainCredentials(self.username, self.password)
            parameter = ConnectionParameters(host=self.host,port=self.port, credentials=credential)
            self.connection = BlockingConnection(parameter)
            print('connected to rabbitmq')
        except exceptions.AMQPConnectionError as e:
            print("Failed to connect", e)

    def is_connected(self):
        return self.connection is not None and self.connection.is_open

    def close(self):
        if self.is_connected():
            self.connection.close()
            self.connection = None
            print('close mq connection')

    def get_channel(self):
        if self.is_connected():
            return self.connection.channel()

        return None
