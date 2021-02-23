from rest_framework import generics

from mainapp.models import City, Street
from mainapp.serializers import CitySerializer, StreetSerializer


class CitiesList(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StreetList(generics.ListAPIView):
    serializer_class = StreetSerializer

    def get_queryset(self):
        city_id = self.kwargs.get('city_id')
        streets = Street.objects.filter(city=city_id)
        return streets
