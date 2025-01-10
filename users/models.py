from django.db import models
from django.contrib.auth.models import User

from constants import MAX_LENGTH, MAX_LENGTH_TEXT




class CreatedDateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    interested_technologies = models.ManyToManyField('Technology', blank=True)
    notifications_enabled = models.BooleanField(default=True)
    preferred_event_types = models.ManyToManyField('EventType', blank=True)


class Organizer(CreatedDateModel):
    name = models.CharField(max_length=MAX_LENGTH)
    description = models.TextField(max_length=MAX_LENGTH_TEXT)
    website = models.URLField(max_length=MAX_LENGTH, blank=True)
    verified = models.BooleanField(default=False)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='organizer_profile'
    )

    def __str__(self):
        return self.name
