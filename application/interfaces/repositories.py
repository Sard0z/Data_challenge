from abc import ABC, abstractmethod
from typing import List

from application.models import Coordinate

class CoordinateRepository(ABC):
    @abstractmethod
    def save_coordinates(self, coordinates: List[Coordinate]):
        pass
    
    @abstractmethod
    def get_coordinates_without_postal_code(self):
        pass

    @abstractmethod
    def save_postal_code_for_coordinates(self,  postal_code_dict):
        pass