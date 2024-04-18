from .models import Coordinate
from application.interfaces.repositories import CoordinateRepository
from application.interfaces.services import PostcodesService
from .exceptions import CoordinateWithoutPostalCodeError
from .exceptions import CSVFileError
import pandas as pd
import logging

logger = logging.getLogger(__name__)


class ProcessFileCSVUseCase:
    def __init__(self, coordinate_repository: CoordinateRepository, post_code: PostcodesService):
        self.coordinate_repository = coordinate_repository
        self.postcodes_service = post_code
    
    def process_csv_file(self, file):
        csv_content_cleaned = file.replace("'", "").replace("\r", "").strip()
        lines = csv_content_cleaned.split('\n')
        data = [line.split('|') for line in lines]
        df = pd.DataFrame(data[1:], columns=data[0])
        coordinates = []
        for _ , row in df.iterrows():
            try:
                latitude = float(row['lat'].replace(',', '.'))
                longitude = float(row['lon'].replace(',', '.'))
                coordinate = Coordinate(latitude=latitude, longitude=longitude)
                coordinates.append(coordinate)

                self.coordinate_repository.save_coordinates(coordinates)
                logger.info("Información guardada en la base de datos correctamente.")
            except Exception as e:
                raise CSVFileError(f"Error processing CSV file: {str(e)}")
        
    

class CompletePostalCodeInformationUseCase():
    def __init__(self, coordinate_repository: CoordinateRepository, postcodes_service: PostcodesService):
        self.coordinate_repository = coordinate_repository
        self.postcodes_service = postcodes_service
        
    def complete_postal_code_information(self):
        coordinates = self.coordinate_repository.get_coordinates_without_postal_code()
        postal_code_dict = {}
        for coordinate in coordinates:
            postal_code = self.postcodes_service.get_postal_code(coordinate.latitude, coordinate.longitude)
            if postal_code:
                postal_code_dict[(coordinate.latitude, coordinate.longitude)] = postal_code[0]
            self.coordinate_repository.save_postal_code_for_coordinates(postal_code_dict)
        if not postal_code_dict:
            raise CoordinateWithoutPostalCodeError("Could not find a postal code for the coordinate.")
        