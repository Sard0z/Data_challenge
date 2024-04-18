# import pytest
# from unittest.mock import Mock
# from application.models import Coordinate
# from infrastructure.repositories import DjangoCoordinateRepository

# @pytest.fixture
# def mock_coordinate_model():
#     return Mock(spec=Coordinate)

# @pytest.fixture
# def mock_coordinate_repository():
#     return Mock(spec=DjangoCoordinateRepository)

# @pytest.mark.django_db
# class TestDjangoCoordinateRepository:

#     def test_save_coordinates(self, mock_coordinate_model, mock_coordinate_repository):
#         # Arrange
#         mock_coordinate = mock_coordinate_model(latitude=52.5, longitude=3.7)
#         mock_coordinates = [mock_coordinate]

#         # Act
#         mock_coordinate_repository.save_coordinates(mock_coordinates)

#         # Assert
#         mock_coordinate.save.assert_called_once()

#     def test_get_coordinates_without_postal_code(self, mock_coordinate_model, mock_coordinate_repository):
#         # Arrange
#         mock_coordinate_model.latitude = 52.5
#         mock_coordinate_model.longitude = 3.7
#         mock_coordinate_model.postal_code = ''

#         mock_coordinate_repository.get_coordinates_without_postal_code.return_value = [mock_coordinate_model]

#         # Act
#         coordinates = mock_coordinate_repository.get_coordinates_without_postal_code()

#         # Assert
#         assert len(coordinates) == 1

#     def test_save_postal_code_for_coordinates(self, mock_coordinate_model, mock_coordinate_repository):
#         # Arrange
#         mock_coordinate_model.save = Mock()

#         mock_coordinate_repository.save_postal_code_for_coordinates({(52.5, 3.7): "12345"})

#         # Assert
#         mock_coordinate_model.save.assert_called_once()
