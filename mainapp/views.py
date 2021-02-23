from rest_framework import generics

from mainapp.models import City
from mainapp.serializers import CitiesSerializer


class CitiesList(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitiesSerializer
