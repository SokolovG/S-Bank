from django.core.validators import MinValueValidator, MaxValueValidator
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
    registered_events = models.ManyToManyField(
        'events.Event',
        related_name='registered_participants',
        blank=True
    )


class Organizer(CreatedDateModel):
    name = models.CharField(max_length=MAX_LENGTH)
    description = models.TextField(max_length=MAX_LENGTH_TEXT)
    website = models.URLField(max_length=MAX_LENGTH, blank=True)
    contact = models.URLField(max_length=MAX_LENGTH, blank=True)
    verified = models.BooleanField(default=False)
    number_of_events = models.PositiveIntegerField(default=0)
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='organizer_profile'
    )

    def __str__(self):
        return self.name
