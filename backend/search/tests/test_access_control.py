from django.contrib.auth.models import User
from django.test import TestCase

class AuthenticatedViewsTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_access_for_authenticated_users(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Make a GET request to the protected view (e.g., dashboard)
        response = self.client.get('/dashboard/')  # Adjust the URL to match your dashboard view URL
        self.assertEqual(response.status_code, 200)  # Ensure the user can access the page and is not redirected
