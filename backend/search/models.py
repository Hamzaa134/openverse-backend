from django.db import models

# Create your models here.

from django.contrib.auth.models import User
# models.py
from django.db import models
from django.contrib.auth.models import User

class RecentSearch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.CharField(max_length=255)
    searched_at = models.DateTimeField(auto_now_add=True)
class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.query} by {self.user.username}"
