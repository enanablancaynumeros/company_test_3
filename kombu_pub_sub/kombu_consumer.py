import os

from kombu import Connection, Queue, Exchange
from kombu.mixins import ConsumerMixin
from workers.tasks.store_event_task import store_gender


farfetch_rabbitmq = os.environ["FARFETCH_QUEUE_URL"]
broker_url = 'amqp://{}'.format(farfetch_rabbitmq)
farfetch_queue_name = os.environ["FARFETCH_QUEUE_NAME"]
exchange = Exchange("farfetch-exchange", type="direct")
queue = Queue(farfetch_queue_name, exchange)


class CustomConsumer(ConsumerMixin):

    def __init__(self, connection, queues):
        self.connection = connection
        self.queues = queues

    def get_consumers(self, Consumer, channel):
        return [
            Consumer(self.queues, callbacks=[self.on_message], accept=['json']),
        ]

    def on_message(self, body, message):
        print("sending task to celery")
        store_gender.delay(body)
        print("will ack")
        message.ack()


def run_consumer():
    with Connection(broker_url, heartbeat=4) as connection:
        consumer = CustomConsumer(connection, [queue])
        consumer.run()


if __name__ == "__main__":
    print("Running the consumer")
    run_consumer()
