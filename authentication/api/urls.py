# urls.py
from django.urls import path

from authentication.api.views import LoginView, RegisterView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    # Add other URLs as needed
]
