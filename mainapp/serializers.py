from rest_framework import serializers
from mainapp.models import City, Street, Shop


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


class ShopSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=255, allow_null=False, allow_blank=False)
    city = CitySerializer(read_only=True)
    street = StreetSerializer(read_only=True)
    apartment = serializers.CharField(max_length=255, allow_null=False, allow_blank=False)
    open_time = serializers.TimeField()
    close_time = serializers.TimeField()

    def create(self, validated_data):
        instance, _ = Shop.objects.get_or_create(**validated_data)
        return instance

    class Meta:
        model = Shop
        fields = '__all__'
