from .models import spatialdata
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework.serializers import HyperlinkedModelSerializer


class spatialdataSerializer(GeoFeatureModelSerializer):
    """ A class to serialize locations as GeoJSON compatible data """

    class Meta:
        model = spatialdata
        geo_field = "coordinates"
        fields = '__all__'
        
        extra_kwargs = {
            "url": {
                "lookup_field": "ISO_A3",
                "view_name": "countrydetail",
            }
        }
                        

