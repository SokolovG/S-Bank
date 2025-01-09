from django.db import models
from django.contrib.auth import get_user_model

from constants import DESCRIPTION_MAX_LENGTH, LOCATION_MAX_LENGTH, MAX_LENGTH

User = get_user_model()

class CreatedDateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Event(CreatedDateModel):
    name = models.CharField(max_length=MAX_LENGTH)
    description = models.TextField(max_length=DESCRIPTION_MAX_LENGTH)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    organizer = models.ForeignKey('Organizer', on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    location = models.ManyToManyField(
        'Location',
        related_name='places'
    )
    is_published = models.BooleanField()
    event_start_date = models.DateTimeField()
    event_end_date = models.DateTimeField()
    category = models.ManyToManyField('Category')
    is_online = models.BooleanField()
    url = models.URLField()
    is_verify = models.BooleanField()
    max_participants = models.PositiveIntegerField(blank=True)
    registration_deadline = models.DateTimeField(blank=True)
    tags = models.ManyToManyField(
        'EventTag',
        blank=True,
        related_name='events')
    format = models.ManyToManyField(
        'EventFormat',
        related_name='formats')

    class Meta:
        ordering = ['event_start_date']

    def __str__(self):
        return self.name


class Location(CreatedDateModel):
    name = models.CharField(max_length=MAX_LENGTH)


class EventFormat(CreatedDateModel):
    format = models.CharField(max_length=MAX_LENGTH)

    def __str__(self):
        return self.format


class EventTag(CreatedDateModel):
    name = models.CharField(max_length=MAX_LENGTH)
    slug = models.SlugField(max_length=MAX_LENGTH, unique=True)

    def __str__(self):
        return self.name


class Category(CreatedDateModel):
    name = models.CharField(max_length=MAX_LENGTH)

    def __str__(self):
        return self.name


class Comment(CreatedDateModel):
    text = models.TextField(max_length=MAX_LENGTH)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
