from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch
import json
from io import BytesIO

class UploadCSVViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    @patch('application.views.process_csv_file_async')
    def test_upload_csv_missing_file(self, mock_process_csv_file_async):
        response = self.client.post(reverse('upload_csv'))

        self.assertEqual(response.status_code, 400)

        expected_error_message = 'No se adjuntó ningún archivo CSV'
        response_data = json.loads(response.content.decode('utf-8'))
        error_message = response_data.get('error', '').lower()
        self.assertIn(expected_error_message.lower(), error_message)


    def test_upload_csv_success(self):
        csv_content = b'lat,lon\n1.0,2.0\n3.0,4.0\n'
        csv_file = BytesIO(csv_content)
        csv_file.name = 'test.csv'
        with patch('application.views.process_csv_file_async') as mock_process_csv:
            response = self.client.post(reverse('upload_csv'), {'csv_file': csv_file}, format='multipart')

        self.assertEqual(response.status_code, 200)
        mock_process_csv.assert_called_once_with(csv_content.decode('utf-8'))



class CompletePostalCodeViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    @patch('application.views.complete_postal_code_information_async')
    def test_complete_postal_code_success(self, mock_complete_postal_code_information_async):
        response = self.client.get(reverse('complete_postal_code'))
        self.assertEqual(response.status_code, 200)
        mock_complete_postal_code_information_async.assert_called_once()

    def test_complete_postal_code_error(self):
        response = self.client.post(reverse('complete_postal_code'))
        self.assertEqual(response.status_code, 400)
