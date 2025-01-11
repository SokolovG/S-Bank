from rest_framework  import viewsets

from .models import Event
from .serializers import EventSelializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSelializer