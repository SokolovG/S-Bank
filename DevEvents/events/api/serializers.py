from rest_framework import serializers

from events.models import Event, Location, Category, Comment
from users.models import Organizer


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['name', 'address', 'city', 'country']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')

class OrganizerSerializer(CategorySerializer):
    class Meta:
        model = Organizer
        exclude = ('user',)

class EventSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    meeting_link = serializers.SerializerMethodField()
    organizer = OrganizerSerializer()
    category = CategorySerializer()

    def get_meeting_link(self, obj):
        if obj.is_online:
            return obj.meeting_link
        else:
            return None

    class Meta:
        model = Event
        exclude = ('author', 'is_published', 'created_at')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('__all__')