from rest_framework import serializers
from mainapp.models import City, Street


class CitySerializer(serializers.Serializer):

    class Meta:
        model = City
        fields = '__all__'

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255, allow_null=False, allow_blank=False)


class StreetSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255, allow_null=False, allow_blank=False)
    city_name = serializers.CharField(source='city.name')

    class Meta:
        model = Street
        fields = '__all__'

