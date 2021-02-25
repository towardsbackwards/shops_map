from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from mainapp.models import City, Street, Shop
from mainapp.serializers import CitySerializer, StreetSerializer, ShopSerializer


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
        city, street, is_open = self.request.GET.get('city'), \
                                self.request.GET.get('street'), \
                                self.request.GET.get('open')
        shops = None
        if is_open == '1':
            shops = Shop.objects.filter(street__city_id=city,
                                        street=street,
                                        open_time__lt=timezone.now().time(),
                                        close_time__gt=timezone.now().time())
        elif is_open == '0':
            shops = Shop.objects.filter(street__city_id=city,
                                        street=street,
                                        open_time__gt=timezone.now().time(),
                                        close_time__lt=timezone.now().time())

        return shops


class ShopCreate(APIView):
    serializer_class = ShopSerializer

    def post(self, request, *args, **kwargs):
        queryset = Shop.objects.create(user=request.user)
        serializer = ShopSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
