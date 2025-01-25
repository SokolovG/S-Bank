"""URL configuration for DevEvents project.

This module defines the root URL patterns for the DevEvents application,
including paths for admin interface and API endpoints.

URL patterns:
    - admin/: Django admin interface
    - api/: REST API endpoints
"""
from drf_spectacular.views import SpectacularAPIView
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('events.api.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
]
