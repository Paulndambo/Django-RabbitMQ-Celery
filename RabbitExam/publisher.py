import os
import pika
import os
import pika
import json
#url = os.environ.get('amqps://student:XYR4yqc.cxh4zug6vje@rabbitmq-exam.rmq3.cloudamqp.com/mxifnklj',
#                     'amqp://guest:guest@localhost:5672/')

url = 'amqps://student:XYR4yqc.cxh4zug6vje@rabbitmq-exam.rmq3.cloudamqp.com/mxifnklj'


class BasePublisher(object):
    def __init__(self, routing_key, body) -> None:
        self.exchange = "exchange.c472be75-f9a0-4dda-84c3-3aaed31f42c6"
        self.queue = "exam"
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
        channel.queue_declare(
            queue=self.queue,
            durable=True,
            exclusive=False,
        )
        channel.queue_bind(self.queue, self.exchange, self.routing_key)

        return channel, connection

    def _publish_message(self):
        channel, connection = self._start_connection()
        channel.basic_publish(
            body=json.dumps(self.body),
            exchange=self.exchange,
            routing_key=self.routing_key,
            properties=pika.BasicProperties(
                delivery_mode = pika.spec.PERSISTENT_DELIVERY_MODE
            )
        )
        channel.close()
        connection.close()

def publish():
    bp = BasePublisher(
        routing_key="c472be75-f9a0-4dda-84c3-3aaed31f42c6",
        body="Hi CloudAMQP, this was fun!"
    )
    bp.run()
publish()