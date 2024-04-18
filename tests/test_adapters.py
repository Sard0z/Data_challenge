import unittest
from unittest.mock import patch, Mock
from infrastructure.adapters import PostcodesAdapter, requests

class TestPostcodesAdapter(unittest.TestCase):

    @patch('infrastructure.adapters.requests.get')
    def test_get_postal_code_success(self, mock_get):
        # Arrange
        adapter = PostcodesAdapter(api_url='https://api.postcodes.io')
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'result': [{'postcode': '12345'}]}
        mock_get.return_value = mock_response

        # Act
        result = adapter.get_postal_code(latitude=52.5, longitude=3.7)

        # Assert
        self.assertEqual(result, ['12345'])


    @patch('infrastructure.adapters.requests.get')
    def test_get_postal_code_no_result(self, mock_get):
        # Arrange
        adapter = PostcodesAdapter(api_url='https://api.postcodes.io')
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response

        # Act
        result = adapter.get_postal_code(latitude=52.5, longitude=3.7)

        # Assert
        self.assertIsNone(result)

    @patch('infrastructure.adapters.requests.get')
    def test_get_postal_code_request_exception(self, mock_get):
        # Arrange
        adapter = PostcodesAdapter(api_url='https://api.postcodes.io')
        mock_get.side_effect = requests.RequestException()

        # Act
        result = adapter.get_postal_code(latitude=52.5, longitude=3.7)

        # Assert
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
