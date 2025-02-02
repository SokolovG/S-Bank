"""URL configuration for events API endpoints.

Defines nested routing for events and their comments using DRF nested routers.
Routes:
   /api/events/
   /api/events/{event_id}/comments/
"""

from django.urls import path, include
from rest_framework_nested import routers

from events.api.views import EventViewSet, EventCommentViewSet

router = routers.DefaultRouter()
router.register('events', EventViewSet, basename='event')

event_comments_router = routers.NestedDefaultRouter(
    router,
    'events',
    lookup='event'
)
event_comments_router.register(
    'comments',
    EventCommentViewSet,
    basename='event-comment'
)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(event_comments_router.urls)),
]
