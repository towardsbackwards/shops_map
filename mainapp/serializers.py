from rest_framework import serializers
from mainapp.models import City


class CitiesSerializer(serializers.Serializer):

    class Meta:
        model = City
        fields = '__all__'

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255, allow_null=False, allow_blank=False)
