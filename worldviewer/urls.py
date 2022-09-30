from django.urls import path
from .views import CountriesListAPI,CountryDetailAPI, home, get_neighbours, get_matching_countries
urlpatterns = [
    path('', home,name='home'),
    path('countrieslistapi', CountriesListAPI.as_view(),name='countrieslist'),
    path('countrydetailapi/<str:ISO_A3>', CountryDetailAPI.as_view(),name='countrydetail'),
    path('matchingcountry/<str:name>', get_matching_countries,name='matching'),
    path('neighbours/<str:name>', get_neighbours,name='neighbours'),
]