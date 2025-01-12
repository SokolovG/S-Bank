from rest_framework import serializers

from .models import Event


class EVentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('__all__')


class EventSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField()

    def get_location(self, obj):
        if obj.is_online:
            return None
        return obj.location

    class Meta:
        model = Event
