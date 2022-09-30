from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import spatialdata
from time import sleep

@shared_task(name="fetch_db")
def downloading_db():
    print('Fetching DB')
    sleep(10)
    queryset=spatialdata.objects.all()
    return queryset