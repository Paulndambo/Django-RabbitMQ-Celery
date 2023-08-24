import pika
import os

url = 'amqps://student:XYR4yqc.cxh4zug6vje@rabbitmq-exam.rmq3.cloudamqp.com/mxifnklj'
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()  # start a channel
channel.queue_declare(
    queue='exam',
    durable=True,
    exclusive=False,
)


def callback(ch, method, properties, body):
  print(' [x] Received ' + str(body))


channel.basic_consume(
    'exam',
    callback,
    auto_ack=True)

print(' [*] Waiting for messages:')
channel.start_consuming()
connection.close()
