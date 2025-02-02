"""Events application models.

This module contains models for managing tech events, locations,
categories and event participation. Core models include Event,
Location, Category, Comment and EventParticipant.
"""

from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from .constants import DESCRIPTION_MAX_LENGTH, LOCATION_MAX_LENGTH, MAX_LENGTH


class CreatedDateModel(models.Model):
    """Abstract base model that adds creation timestamp."""

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Define model as abstract."""

        abstract = True


class Location(CreatedDateModel):
    """Model representing a physical location for events.

    Stores address information including city and country.
    """

    name = models.CharField(max_length=MAX_LENGTH)
    address = models.CharField(max_length=LOCATION_MAX_LENGTH, blank=True)
    city = models.CharField(max_length=MAX_LENGTH)
    country = models.CharField(max_length=MAX_LENGTH)

    def __str__(self):
        """Return string representation of Location."""
        return self.name


class Category(CreatedDateModel):
    """Model representing event categories.

    Each category has a unique slug and optional description.
    """

    name = models.CharField(max_length=MAX_LENGTH)
    slug = models.SlugField(max_length=MAX_LENGTH, unique=True)
    description = models.TextField(
        blank=True,
        max_length=DESCRIPTION_MAX_LENGTH
    )

    def __str__(self):
        """Return string representation of Category."""
        return self.name


class Event(CreatedDateModel):
    """Model representing a tech event or meetup.

    Attributes:
        name (str): Event title
        description (str): Detailed event description
        author (User): User who created the event
        organizer (Organizer): Organization hosting the event
        pub_date (datetime): When event was published
        location (Location): Physical location for offline events
        is_published (bool): Whether event is publicly visible
        event_start_date (datetime): When event begins
        event_end_date (datetime): When event ends
        category (Category): Event category/topic
        is_online (bool): Whether event is online or offline
        meeting_link (URL): Link for online events
        is_verify (bool): Whether event is verified
        max_participants (int): Maximum number of attendees
        registration_deadline (datetime): Last date to register
        format (str): Event format type
        members (int): Current number of participants
        photos (ImageField): Event images
        participants (M2M): Users registered for event
    """

    name = models.CharField(max_length=MAX_LENGTH)
    description = models.TextField(max_length=DESCRIPTION_MAX_LENGTH)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    organizer = models.ForeignKey('users.Organizer', on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    location = models.ForeignKey(
        Location,
        related_name='places',
        on_delete=models.CASCADE
    )
    is_published = models.BooleanField()
    event_start_date = models.DateTimeField()
    event_end_date = models.DateTimeField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='categories'
    )
    is_online = models.BooleanField()
    meeting_link = models.URLField()
    is_verify = models.BooleanField()
    max_participants = models.PositiveIntegerField(blank=True)
    registration_deadline = models.DateTimeField(blank=True)
    format = models.CharField(max_length=MAX_LENGTH)
    members = models.PositiveIntegerField(blank=True)
    photos = models.ImageField()
    participants = models.ManyToManyField(
        User,
        through='EventParticipant',
        related_name='participated_events'
    )

    class Meta:
        """Specify default ordering."""

        ordering = ['event_start_date']

    def __str__(self):
        """Return string representation of Event."""
        return self.name

    def clean(self):
        """Validate event data before saving.

        Raises:
            ValidationError: If dates are invalid,
                online/offline requirements not met.
        """
        if self.event_start_date < self.event_end_date:
            raise ValidationError(
                'The end date cannot be earlier than the start date.'
            )
        if (self.registration_deadline
                and self.registration_deadline > self.event_start_date):
            raise ValidationError(
                'The deadline for registration should be before the event starts.'
            )

        if self.is_online and not self.meeting_link:
            raise ValidationError(
                'For the online event, a link is required.'
            )

        if not self.is_online and not self.location:
            raise ValidationError(
                'For an offline event, the venue must be specified.'
            )

    def is_user_participant(self, user):
        """Check if user is participant in this event."""
        return EventParticipant.objects.filter(
            event=self,
            user=user
        ).exists()


class Comment(CreatedDateModel):
    """Model for event comments.

    Links users' comments to specific events.
    """

    text = models.TextField(max_length=MAX_LENGTH)
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return truncated comment text."""
        return self.text


class EventParticipant(CreatedDateModel):
    """Model tracking event participation status.

    Records registration date and status for each participant.
    """

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='participant_records'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='event_participations'
    )
    status = models.CharField(max_length=MAX_LENGTH)
    registration_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Define uniqueness constraint."""

        unique_together = ['event', 'user']

    def __str__(self):
        """Return string representation of participation."""
        return f"{self.user.username} - {self.event.name} - {self.status}"
