from rest_framework import serializers

from events.models import Event, Location, Category, Comment
from events.utils import to_camel_case, to_snake_case
from users.models import Organizer


class CamelCaseSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        result = super().to_representation(instance)
        camel_case_data = {}
        for key, value in result.items():
            camel_case_data[to_camel_case(key)] = value

        return camel_case_data

    def to_internal_value(self, data):
        snake_case_data = {}
        for key, value in data.items():
            snake_case_data[to_snake_case(key)] = value

        return super().to_internal_value(snake_case_data)

class LocationSerializer(CamelCaseSerializer):
    class Meta:
        model = Location
        fields = ['name', 'address', 'city', 'country']

class CategorySerializer(CamelCaseSerializer):
    class Meta:
        model = Category
        fields = ('__all__')

class OrganizerSerializer(CategorySerializer):
    class Meta:
        model = Organizer
        exclude = ('user',)

class EventSerializer(CamelCaseSerializer):
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

class CommentSerializer(CamelCaseSerializer):
    class Meta:
        model = Comment
        fields = ('__all__')