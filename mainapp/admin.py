from django.contrib import admin
from mainapp.models import City, Shop, Street


class CityAdmin:
    fields = '__all__'



admin.site.register(City)
admin.site.register(Street)
admin.site.register(Shop)
