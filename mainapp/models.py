from django.db import models
from django.utils import timezone


class City(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name_plural = 'Cities'

    def __str__(self):
        return f'{self.name} city, (id={self.pk})'


class Street(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Shop(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    apartment = models.CharField(max_length=255, null=False, blank=False)
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self):
        return f'{self.name}'
