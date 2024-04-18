# import unittest
# from unittest.mock import MagicMock
# from asynctest import TestCase, MagicMock, CoroutineMock, patch
# from application.tasks import process_csv_file_async, complete_postal_code_information_async

# class TestProcessCSVFileAsync(TestCase):
#     @patch('application.tasks.ProcessFileCSVUseCase')
#     @patch('application.tasks.PostcodesServiceImpl')
#     @patch('application.tasks.DjangoCoordinateRepository')
#     async def test_process_csv_file_async_success(self, MockCoordinateRepository, MockPostcodesService, MockProcessFileCSVUseCase):
#         csv_content = "latitude,longitude\n1.23,4.56\n7.89,0.12"
#         mock_use_case_instance = MagicMock()
#         mock_use_case_instance.process_csv_file = CoroutineMock()
#         MockProcessFileCSVUseCase.return_value = mock_use_case_instance
#         await process_csv_file_async(csv_content)
#         MockCoordinateRepository.assert_called_once()
#         MockPostcodesService.assert_called_once_with(api_url='https://api.postcodes.io')
#         MockProcessFileCSVUseCase.assert_called_once_with(MockCoordinateRepository.return_value, MockPostcodesService.return_value)
#         mock_use_case_instance.process_csv_file.assert_called_once_with(file=csv_content)

#     async def test_process_csv_file_async_error(self):
#         csv_content = "latitude,longitude\n1.23,4.56\n7.89,0.12"
#         with self.assertRaises(Exception):
#             await process_csv_file_async(None)


# class TestCompletePostalCodeInformationAsync(TestCase):
#     @patch('application.tasks.CompletePostalCodeInformationUseCase')
#     @patch('application.tasks.PostcodesServiceImpl')
#     @patch('application.tasks.DjangoCoordinateRepository')
#     async def test_complete_postal_code_information_async_success(self, MockCoordinateRepository, MockPostcodesService, MockCompletePostalCodeInformationUseCase):
#         mock_use_case_instance = MagicMock()
#         mock_use_case_instance.complete_postal_code_information = CoroutineMock()
#         MockCompletePostalCodeInformationUseCase.return_value = mock_use_case_instance
#         response = await complete_postal_code_information_async()
#         MockCoordinateRepository.assert_called_once()
#         MockPostcodesService.assert_called_once_with(api_url='https://api.postcodes.io')
#         MockCompletePostalCodeInformationUseCase.assert_called_once_with(MockCoordinateRepository.return_value, MockPostcodesService.return_value)
#         mock_use_case_instance.complete_postal_code_information.assert_called_once()
#         self.assertEqual(response.status_code, 200)

#     async def test_complete_postal_code_information_async_error(self):
#         with self.assertRaises(Exception):
#             await complete_postal_code_information_async()


# if __name__ == '__main__':
#     unittest.main()
