from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

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


class ShopCreate(generics.CreateAPIView):
    serializer_class = ShopSerializer

    def post(self, request, *args, **kwargs):
        queryset = Shop.objects.create(user=request.user)
        serializer = ShopSerializer(queryset, data=request.data)
        if serializer.is_valid():
            return Response({'serializer': serializer, 'queryset': queryset})

        serializer.save()
    #
    #     return redirect('/api/v1/cars/usercars/')
    #
    # def perform_create(self, serializer):
    #     author = get_object_or_404(Shop, id=self.request.data.get('author_id'))
    #     return serializer.save(author=author)