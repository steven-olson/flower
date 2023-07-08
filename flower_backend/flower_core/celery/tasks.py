from celery import Celery, shared_task
from flower_core import celery_app


@celery_app.task
def add(x, y):
    return x + y


@celery_app.task
def echo(msg):
    print(f"MSG: {msg}")
    return msg
