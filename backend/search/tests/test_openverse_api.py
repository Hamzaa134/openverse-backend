from django.test import TestCase
from unittest.mock import patch
from openverse_backend.services.openverse_api import OpenverseAPI

class SearchMediaTest(TestCase):

    @patch('openverse_backend.services.openverse_api.requests.get')
    def test_search_media(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "results": [
                {"title": "Test Image", "url": "http://example.com/test.jpg"}
            ]
        }

        results = OpenverseAPI.search_media("nature", media_type="image")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["title"], "Test Image")
