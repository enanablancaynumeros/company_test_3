from celery import Celery

celery_app = Celery('workers')

celery_app.config_from_object('workers.celeryconfig')
