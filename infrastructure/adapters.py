import time
import requests
import logging

class PostcodesAdapter:
    def __init__(self, api_url):
        self.api_url = api_url
        self.logger = logging.getLogger(__name__)

    def get_postal_code(self, latitude, longitude):
        for attempt in range(3):
            try:
                url = f"{self.api_url}/postcodes?lon={longitude}&lat={latitude}"
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()
                if 'result' in data:
                    postcodes = [result['postcode'] for result in data['result']]
                    return postcodes
                else:
                    return None
            except requests.RequestException as e:
                if attempt < 2: 
                    wait_time = 2 ** attempt
                    time.sleep(wait_time)
                else:
                    self.logger.error(f"Error en la solicitud de códigos postales: {e}")
