from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from .services.openverse_api import OpenverseAPI
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View
from search.models import SearchHistory
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.utils.timezone import now
from datetime import timedelta

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '🎉 Account created successfully! You can now log in.')
            return redirect('login')  # Redirecting to the login page after registration
        return render(request, 'register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = AuthenticationForm
    def get_success_url(self):
        return reverse_lazy('dashboard')
class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'dashboard.html')


class SearchMediaView(View):
    def get(self, request):
        query = request.GET.get("q", "")
        license = request.GET.get("license", "")
        media_type = request.GET.get("media_type", "")

        if media_type == "all" or not media_type:
            media_type = None

        results = OpenverseAPI.search_media(query, license, media_type)

        if request.user.is_authenticated and query:
            # Check if the same query has been saved in the last X minutes (e.g., 5 min)
            five_minutes_ago = now() - timedelta(minutes=5)
            already_exists = SearchHistory.objects.filter(
                user=request.user,
                query=query,
                timestamp__gte=five_minutes_ago
            ).exists()

            if not already_exists:
                SearchHistory.objects.create(user=request.user, query=query)

        return JsonResponse({"results": results})


class SearchHistoryView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')

        searches = SearchHistory.objects.filter(user=request.user).order_by('-timestamp')
        return render(request, 'saved_searches.html', {'searches': searches})


class DeleteSearchView(View):
    @method_decorator(csrf_exempt)
    def post(self, request, pk):
        if request.user.is_authenticated:
            SearchHistory.objects.filter(pk=pk, user=request.user).delete()
        return redirect('saved-searches')
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
