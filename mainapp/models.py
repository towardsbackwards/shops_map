from django.db import models


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
    street = models.CharField(max_length=255, null=False, blank=False)
    apartment = models.CharField(max_length=255, null=False, blank=False)
    open_time = models.DateTimeField()
    close_time = models.DateTimeField()

    def __str__(self):
        return f'{self.name}'
