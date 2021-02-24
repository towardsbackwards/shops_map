from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from mainapp.models import City, Street, Shop
from mainapp.serializers import CitySerializer, StreetSerializer, ShopSerializer, ShopListSerializer


class CitiesList(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StreetList(generics.ListAPIView):
    serializer_class = StreetSerializer

    def get_queryset(self):
        city_id = self.kwargs.get('city_id')
        streets = Street.objects.filter(city=city_id)
        return streets


class ShopList(generics.ListAPIView):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()

    def get_queryset(self):
        city, street = self.request.query_params.get('city'), self.request.query_params.get('street')
        is_open = self.request.query_params.get('open')
        Shops = Shop.objects.filter(street__city_id=city, street=street)
        return Shops


class ShopCreate(APIView):
    serializer_class = ShopSerializer

    def post(self, request, *args, **kwargs):
        queryset = Shop.objects.create(user=request.user)
        serializer = ShopSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
