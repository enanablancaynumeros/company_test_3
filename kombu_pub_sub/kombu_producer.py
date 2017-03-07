from kombu import Connection
from kombu.pools import producers
from kombu_consumer import broker_url, exchange


def publish_message(message):
    with Connection(broker_url) as connection:
        with producers[connection].acquire(block=True) as producer:
            print("Publishing the message {}".format(message))
            producer.publish(message,
                             serializer='json',
                             exchange=exchange,
                             declare=[exchange],
                             )
            return True
