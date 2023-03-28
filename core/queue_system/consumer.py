import pika
import os
import json
url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/')

from notifications.routing_keys import ROUTING_KEYS
from notifications.consumer_methods import NotificationConsumer


class BaseConsumer(object):
    exchange = "test_exchange"
    exchange_type = "direct"
    queue = "test_queue"
    consumer_name = None
    
    def __init__(self):
        self.url = url
    #    self.exchange = "test_exchange"
    #    self.queue = "test_queue"
        #self.routing_key = routing_key
        #self.body = body

    def init_consumer(self):
        self.__make_connection()
        self.__queue_declare()
        self.__exchange_declare()
        self.__bind_queue()
        #self._consume_message()

    def base_consume(self):
        self.channel.basic_consume(self.queue, self.__callback, auto_ack=True)
        self.channel.start_consuming()


    def __make_connection(self):
        params = pika.URLParameters(url)
        self.connection = pika.BlockingConnection(params)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue)
        
        #return channel, connection

    def __queue_declare(self):
        self.channel.queue_declare(queue=self.queue)


    def __exchange_declare(self):
        self.channel.exchange_declare(
            exchange=self.exchange, exchange_type=self.exchange_type)


    def __callback(self, ch, method, properties, body):
        for consumer_method in ROUTING_KEYS[self.consumer_name][method.routing_key]:
            NotificationConsumer.body = body
            getattr(NotificationConsumer, consumer_method)()
           
              
    def __bind_queue(self):
        for key in ROUTING_KEYS:
            self.channel.queue_bind(queue=self.queue, exchange=self.exchange, routing_key=key)

#bc = BaseConsumer()
#bc.init_consumer()