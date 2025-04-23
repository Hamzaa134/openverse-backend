from django.contrib import admin
from django.urls import path, include
from . import views  # 👈 Import the views.py file
from .views import IndexView
from .views import RegisterView
from .views import CustomLoginView, DashboardView
from .views import SearchMediaView
from .views import LogoutView
from .views import SearchHistoryView
from .views import DeleteSearchView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', include('search.urls')),
    
    path('', IndexView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'), 
    path('api/search/', SearchMediaView.as_view(), name='search-media'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('saved-searches/', SearchHistoryView.as_view(), name='saved-searches'),
    path('delete-search/<int:pk>/', DeleteSearchView.as_view(), name='delete-search'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('complete/google/', include('social_django.urls', namespace='social')),

]

