from abc import ABC, abstractmethod

class PostcodesService(ABC):
    @abstractmethod
    def get_postal_code(self, latitude, longitude):
        pass