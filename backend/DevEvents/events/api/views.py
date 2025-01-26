"""ViewSets for handling Event and Comment API endpoints.

Provides CRUD operations for Events and their associated Comments
through REST API endpoints.
"""

from rest_framework import viewsets
from django.shortcuts import get_object_or_404, get_list_or_404

from events.models import Event
from events.api.serializers import EventSerializer, CommentSerializer


class EventViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing Event instances."""
    queryset = Event.objects.select_related(
        'location',
        'organizer',
        'category'
    ).all()
    serializer_class = EventSerializer
    

class EventCommentViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing Event Comments."""
    serializer_class = CommentSerializer

    def get_queryset(self):
        """Return queryset of comments for specific event."""
        post = get_object_or_404(Event, id=self.kwargs.get('event_pk'))
        return get_list_or_404(post.comments.all())
