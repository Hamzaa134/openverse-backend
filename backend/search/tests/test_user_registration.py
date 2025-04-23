from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User

class UserRegistrationTest(TestCase):
    def test_user_can_register(self):
        # Create POST data for registration
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'StrongPassword123',
            'password2': 'StrongPassword123'
        })
        # Assert successful redirection after registration
        self.assertEqual(response.status_code, 302)
        # Verify if the user was created
        self.assertTrue(User.objects.filter(username='testuser').exists())
