"""ViewSets for handling Event and Comment API endpoints.

Provides CRUD operations for Events and their associated Comments
through REST API endpoints.
"""

from rest_framework import viewsets
from django.shortcuts import get_object_or_404, get_list_or_404

from events.models import Event
from events.api.serializers import EventListSerializer, EventDetailSerializer, CommentSerializer


class EventViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing Event instances."""
    def get_queryset(self):
        event_id = self.kwargs.get('pk')
        if self.action == 'list':
            return Event.objects.select_related('location').only('id',
                                                                'name',
                                                                'location__name',
                                                                'event_start_date',
                                                                'max_participants',
                                                                'description'
                                                                )

        elif self.action == 'retrieve':
            return Event.objects.filter(id=event_id).prefetch_related('participants').select_related('category', 'location')
        
        elif self.action in ['update', 'partial_update', 'destroy']:
            return Event.objects.filter(id=event_id)

        return queryset.none()

    def get_serializer_class(self):
        if self.action == 'list':
            return EventListSerializer

        return EventDetailSerializer
        
    

class EventCommentViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing Event Comments."""
    serializer_class = CommentSerializer

    def get_queryset(self):
        """Return queryset of comments for specific event."""
        post = get_object_or_404(Event, id=self.kwargs.get('event_pk'))
        return get_list_or_404(post.comments.all())
