from django.urls import path

from mainapp.views import CitiesList

app_name = 'main'

urlpatterns = [
    path('city/', CitiesList.as_view(), name='cities'),
]
