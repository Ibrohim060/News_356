from django.urls import path
from .views import (
    login_view,
    register_view,
)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
]
# This code defines the URL patterns for a Django application. Each URL pattern is associated with a specific view function that handles requests to that URL. The urlpatterns list contains all the defined URL patterns, and each pattern is created using the path() function, which takes the URL path, the view function, and an optional name for the URL pattern.

