from django.contrib.gis import admin
from .models import spatialdata

admin.site.register(spatialdata, admin.ModelAdmin)