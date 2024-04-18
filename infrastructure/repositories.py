from application.models import Coordinate as CoordinateModel
from application.interfaces.repositories import CoordinateRepository

class DjangoCoordinateRepository(CoordinateRepository):
    def save_coordinates(self, coordinates):
        for coordinate in coordinates:
            coordinate_model = CoordinateModel(
                latitude=coordinate.latitude,
                longitude=coordinate.longitude
            )
            coordinate_model.save()

    def get_coordinates_without_postal_code(self):
        return CoordinateModel.objects.exclude(postal_code='').exclude(longitude=None).exclude(latitude=None)
    
    def save_postal_code_for_coordinates(self, postal_code_dict):
        for (latitude, longitude), postal_code in postal_code_dict.items():
            coordinate_model = CoordinateModel.objects.filter(latitude=latitude, longitude=longitude).first()
            if coordinate_model:
                coordinate_model.postal_code = postal_code
                coordinate_model.save()
