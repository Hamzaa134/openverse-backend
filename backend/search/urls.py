from django.urls import path
from .views import search_media

urlpatterns = [
    path('search/', search_media, name='search'),  # It's a good practice to add a more descriptive path
]
