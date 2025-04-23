from django.contrib.auth.models import User
from search.models import RecentSearch
from django.test import TestCase

class RecentSearchTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='StrongPassword123')

    def test_create_recent_search(self):
        # Save a recent search
        search = RecentSearch.objects.create(user=self.user, query="nature")
        self.assertEqual(search.query, "nature")
        self.assertEqual(search.user.username, "testuser")

    def test_delete_recent_search(self):
        # Save and delete a recent search
        search = RecentSearch.objects.create(user=self.user, query="mountains")
        search.delete()
        self.assertEqual(RecentSearch.objects.count(), 0)  # Ensure search is deleted
