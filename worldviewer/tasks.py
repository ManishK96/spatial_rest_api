from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import spatialdata
import json
import os
import pathlib
from time import sleep
from .serializers import spatialdataSerializer
from rest_framework.parsers import JSONParser


@shared_task(name="downloading_db")
def downloading_db():
    print('Fetching DB')
    path = pathlib.Path().absolute()
    file = os.path.join(path, 'worldviewer\data\countries.geojson')
    with open(file, 'r') as f:
        data = json.load(f)

    features = data=data["features"]
    for feature in features:
        s_data = spatialdataSerializer(data=feature)
        if s_data.is_valid():
            s_data.save()
        
   

