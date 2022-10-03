from __future__ import absolute_import, unicode_literals
import os
import kombu
from celery import Celery, bootsteps
# set the default Django settings module for the 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spatialapi.settings')
app = Celery('worldviewer')
app.config_from_object('django.conf:settings', namespace='CELERY')
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
