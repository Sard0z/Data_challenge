from django.db import models


class PostalCode(models.Model):
    postal_code = models.CharField(max_length=20)
    latitude = models.FloatField()
    longitude = models.FloatField()
    country = models.CharField(max_length=100)
