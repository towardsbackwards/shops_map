from django.urls import path

from mainapp.views import CitiesList, StreetList

app_name = 'main'

urlpatterns = [
    path('city/', CitiesList.as_view(), name='cities'),
    path('city/<int:city_id>/street/', StreetList.as_view(), name='streets')
]
