from django.db import models


class Coordinate(models.Model):
    latitude = models.CharField(max_length=20, default='00000')
    longitude = models.CharField(max_length=20, default='00000')
    postal_code = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return f"({self.latitude}, {self.longitude})"
    
    class Meta:
        app_label = 'application'
