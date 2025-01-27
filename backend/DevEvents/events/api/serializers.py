"""Serializers for Event-related models in the DevEvents API.

Contains serializers for Location, Category, Organizer, Event, and Comment models,
defining how model instances are converted to/from JSON.
"""

from rest_framework import serializers

from events.models import Event, Location, Category, Comment
from users.models import Organizer


class LocationSerializer(serializers.ModelSerializer):
    """Serializer for Location model."""
    class Meta:
        model = Location
        fields = ['name', 'address', 'city', 'country']

class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category model."""
    class Meta:
        model = Category
        fields = '__all__'

class OrganizerSerializer(CategorySerializer):
    """Serializer for Organizer model, inheriting from CategorySerializer."""
    class Meta:
        model = Organizer
        exclude = ('user',)

class EventListSerializer(serializers.ModelSerializer):
    """Serializer for Event model with nested serializers for related fields."""
    location = LocationSerializer()
    meeting_link = serializers.SerializerMethodField()
    organizer = OrganizerSerializer()
    category = CategorySerializer()

    def get_meeting_link(self, obj):
        """Return meeting link only for online events."""
        return obj.meeting_link if obj.is_online else None

    class Meta:
        model = Event
        exclude = ('author', 'is_published', 'created_at')


class EventDetailSerializer(serializers.ModelSerializer):
    Location = LocationSerializer()
    class Meta:
        model = Event
        fields = (
            'name',
            'event_start_date',
            'location__name',
            'max_participants',
            'description'
        )

class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment model."""
    class Meta:
        model = Comment
        fields = '__all__'