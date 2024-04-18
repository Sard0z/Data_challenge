from .adapters import PostcodesAdapter
from application.interfaces.services import PostcodesService

class PostcodesServiceImpl(PostcodesService):
    def __init__(self, api_url):
        self.adapter = PostcodesAdapter(api_url)
    
    def get_postal_code(self, latitude, longitude):
        return self.adapter.get_postal_code(latitude, longitude)