import os
from celery import Celery
from flower_core.celery import celery_config

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "flower_core.settings")
app = Celery("flower_celery")
app.config_from_object(celery_config, namespace="CELERY")
app.autodiscover_tasks()
