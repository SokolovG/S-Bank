"""Models for user profiles and organizers in the events platform."""

from decimal import Decimal

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User

from .constants import MAX_LENGTH, MAX_LENGTH_TEXT


class CreatedDateModel(models.Model):
    """Base model class that automatically records creation date."""

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta options for CreatedDateModel."""

        abstract = True


class Profile(models.Model):
    """User profile model with additional user.

    information and event registrations.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    interested_technologies = models.CharField(blank=True, max_length=50)
    notifications_enabled = models.BooleanField(default=True)
    registered_events = models.ManyToManyField(
        'events.Event',
        related_name='registered_participants',
        blank=True
    )


class Organizer(CreatedDateModel):
    """Model for event organizers with verification and rating system."""

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
        validators=[MinValueValidator(Decimal(0)),
                    MaxValueValidator(Decimal(5))]
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='organizer_profile'
    )

    def __str__(self):
        """Return string representation of Organizer."""
        return self.name
