from rest_framework.routers import DefaultRouter
from django.urls import path, include

from events.api.views import EventViewSet


router = DefaultRouter()
router.register('events', EventViewSet, basename='event')


urlpatterns = [
    path('events', include(router.urls)),

]