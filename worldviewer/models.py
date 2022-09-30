from django.contrib.gis.db import models
from django_extensions.db.fields import AutoSlugField
from django_celery_beat.models import PeriodicTask


class spatialdata(models.Model):
    ADMIN = models.CharField(max_length=50, blank =True)
    ISO_A3 = models.CharField(max_length=3, blank = True)
    coordinates = models.GeometryField(srid=4326, null=True, blank=True)

