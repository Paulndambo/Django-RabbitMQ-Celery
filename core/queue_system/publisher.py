import os
import pika
import os, pika
import json
url = os.environ.get('CLOUDAMQ_URL', 'amqp://guest:guest@localhost:5672/')


class BasePublisher(object):
    def __init__(self, routing_key, body) -> None:
        self.exchange = "test_exchange"
        self.queue = "test_queue"
        self.routing_key = routing_key
        self.url = url
        self.body = body

    def run(self):
        self._start_connection()
        self._publish_message()
        

    def _start_connection(self):
        params = pika.URLParameters(self.url)
        connection = pika.BlockingConnection(params)
        channel = connection.channel()

        channel.exchange_declare(self.exchange)
        channel.queue_declare(queue=self.queue)
        channel.queue_bind(self.queue, self.exchange, self.routing_key)

        return channel, connection

    def _publish_message(self):
        channel, connection = self._start_connection()
        channel.basic_publish(
            body=json.dumps(self.body),
            exchange=self.exchange,
            routing_key=self.routing_key
        )
        channel.close()
        connection.close()


def publish():
    bp = BasePublisher(
        routing_key="tests",
        body={
            "name": "Paul Ndambo",
            "age": 24,
            "school": "Masinde Muliro University of Sci. & Tech.",
            "specialty": "Cloud, Backend & DevOps Software Engineer"
        })
    bp.run()

publish()
