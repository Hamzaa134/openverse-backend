from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User

class UserLoginTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='StrongPassword123')

    def test_user_can_login(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'StrongPassword123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after login
        self.assertRedirects(response, '/dashboard/')  # Check if redirected to dashboard
