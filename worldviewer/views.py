from django.shortcuts import render
from .models import spatialdata
from .serializers import spatialdataSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView 
#from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from . import tasks

from rest_framework_gis.filterset import GeoFilterSet
from rest_framework_gis.filters import GeometryFilter
from django_filters import filters

class CountriesListAPI(ListCreateAPIView):

    queryset = spatialdata.objects.all()
    serializer_class = spatialdataSerializer

class CountryDetailAPI(RetrieveUpdateDestroyAPIView):

    queryset = spatialdata.objects.all()
    serializer_class = spatialdataSerializer
    lookup_field = "ISO_A3"

'''
@csrf_exempt
def countrieslistapi(request):
    if request.method == 'GET':
        snippets = models.spatialdata.objects.all()
        serializer = serializers.spatialdataSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializers.spatialdataSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

'''

# Create your views here.
def home(request):
    world_data = spatialdata.objects.all()
    context = {
        "world_data":world_data
    }
    return render(request, 'base.html',context)


#Non spatial query

def get_matching_countries(self, str):

    countries = []
    for data in (spatialdata.objects.filter(ADMIN__icontains=name)):
        countries.append(data.ADMIN)
    if len(countries):
        return JsonResponse(countries, status= 200, safe=False)
    return JsonResponse(response = 404)


#Spatial query
def get_neighbours(self, name):

    country = spatialdata.objects.get(ADMIN=name)
    neighbours = []
    for data in (spatialdata.objects.filter(coordinates__touches=country.coordinates)):
        neighbours.append(data.ADMIN)
    if len(neighbours):
        return JsonResponse(neighbours, status = 200, safe=False)
    return JsonResponse(response = 404)








