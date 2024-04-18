import re
from math import sqrt

from django.db import models


class PostalCode:
    def __init__(self, code, latitude, longitude, details) -> None:
        self.code,
        self.latitude,
        self.longitude,
        self.details

    def __str__(self) -> str:
        return f"PostalCode: {self.code}, Latitude: {self.latitude}, Longitude: {self.longitude}, Details: {self.details}"
    
    def validate_postal_code(self):
        pattern = r'^[A-Za-z]{2}\d{1,2}(?:\s\d[A-Za-z]{2})?$'
        return bool(re.match(pattern, self.code))

    def calculate_distance(self, other_postal_code):
        return sqrt((self.latitude - other_postal_code.latitude)**2 + (self.longitude - other_postal_code.longitude)**2)
    