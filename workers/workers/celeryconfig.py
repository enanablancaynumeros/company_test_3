import os

broker_url = 'amqp://{}'.format(os.environ.get("CELERY_RABBITMQ_URL"))
print("Using broker {}".format(broker_url))
result_backend = 'rpc://'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'UTC'
enable_utc = True
worker_concurrency = 4
include = ['workers.tasks.store_event_task']
task_always_eager = False
