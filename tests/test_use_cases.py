# import pytest
# from unittest.mock import Mock, patch
# from application.use_cases import ProcessFileCSVUseCase, CompletePostalCodeInformationUseCase, Coordinate, CSVFileError, CoordinateWithoutPostalCodeError
# import tempfile


# @pytest.fixture
# def mock_coordinate_repository():
#     return Mock()

# @pytest.fixture
# def mock_postcodes_service():
#     return Mock()

# def test_process_csv_file_successful(mock_coordinate_repository, mock_postcodes_service):
#     use_case = ProcessFileCSVUseCase(mock_coordinate_repository, mock_postcodes_service)
#     file_content = "lat|lon\n52.5|3.7\n51.2|4.8"
    
#     with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
#         temp_file.write(file_content)
#         temp_file_path = temp_file.name

#     with open(temp_file_path, 'r') as f:
#         csv_content = f.read()
#         use_case.process_csv_file(csv_content)
    

#     assert mock_coordinate_repository.save_coordinates.call_count == 2

# def test_process_csv_file_with_error(mock_coordinate_repository, mock_postcodes_service):
#     use_case = ProcessFileCSVUseCase(mock_coordinate_repository, mock_postcodes_service)
#     file_content = "lat|lon\ninvalid|data"
    
#     with pytest.raises(CSVFileError):
#         use_case.process_csv_file(file_content)

# def test_complete_postal_code_information_successful(mock_coordinate_repository, mock_postcodes_service):
#     use_case = CompletePostalCodeInformationUseCase(mock_coordinate_repository, mock_postcodes_service)
    
#     mock_coordinate_repository.get_coordinates_without_postal_code.return_value = [
#         Coordinate(latitude=52.5, longitude=3.7),
#         Coordinate(latitude=51.2, longitude=4.8)
#     ]

#     mock_postcodes_service.get_postal_code.side_effect = ["12345", "67890"]

#     use_case.complete_postal_code_information()

#     assert mock_postcodes_service.get_postal_code.call_count == 2
#     assert mock_coordinate_repository.save_postal_code_for_coordinates.call_count == 2


# def test_complete_postal_code_information_with_error(mock_coordinate_repository, mock_postcodes_service):
#     mock_coordinate_repository.get_coordinates_without_postal_code.return_value = []
#     use_case = CompletePostalCodeInformationUseCase(mock_coordinate_repository, mock_postcodes_service)
    
#     with pytest.raises(CoordinateWithoutPostalCodeError):
#         use_case.complete_postal_code_information()
