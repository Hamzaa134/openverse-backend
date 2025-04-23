import requests

class OpenverseAPI:
    BASE_URL = "https://api.openverse.engineering/v1/"

    @staticmethod
    def search_media(query, license=None, media_type=None):
        # If media_type is "all", query both images and audio endpoints
        if media_type == "all" or media_type is None:
            # Combine results from both image and audio endpoints
            image_results = OpenverseAPI._search_images(query, license)
            audio_results = OpenverseAPI._search_audio(query, license)
            results = image_results + audio_results  # Combine both results
        elif media_type == "audio":
            results = OpenverseAPI._search_audio(query, license)
        else:
            # Default to images if media_type is "image" or unrecognized
            results = OpenverseAPI._search_images(query, license)
        
        # Add media_type to the result
        for item in results:
            item["media_type"] = media_type or "image"  # Ensure media_type is set
        
        return results

    @staticmethod
    def _search_images(query, license=None):
        """Fetch image results from Openverse API"""
        return OpenverseAPI._search(query, license, "images/")

    @staticmethod
    def _search_audio(query, license=None):
        """Fetch audio results from Openverse API"""
        return OpenverseAPI._search(query, license, "audio/")

    @staticmethod
    def _search(query, license, endpoint):
        """Helper function to perform the actual API request"""
        url = OpenverseAPI.BASE_URL + endpoint
        params = {
            "q": query,
            "license": license,
            "page_size": 20
        }

        # Remove keys with None or empty string values
        params = {k: v for k, v in params.items() if v}

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get("results", [])

        except requests.RequestException as e:
            print(f"Openverse API error: {e}")
            return []
