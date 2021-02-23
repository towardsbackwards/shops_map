from django.urls import path

from mainapp.views import CitiesList, StreetList, ShopCreate

app_name = 'main'

urlpatterns = [
    path('city/', CitiesList.as_view(), name='cities'),
    path('city/<int:city_id>/street/', StreetList.as_view(), name='streets'),
    path('shop/', ShopCreate.as_view(), name='add_shop'),
]
