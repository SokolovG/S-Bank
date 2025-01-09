from django.db import models
from django.contrib.auth import get_user_model

from constants import NAME_MAX_LENGTH, DESCRIPTION_MAX_LENGTH, CATEGORY_MAX_LENGTH, ORGANIZER_NAME_MAX_LENGTH, COMMENT_MAX_LENGTH, LOCATION_MAX_LENGTH

User = get_user_model()

class CreatedDateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Event(CreatedDateModel):
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    description = models.TextField(max_length=DESCRIPTION_MAX_LENGTH)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    organizer = models.ForeignKey('Organizer', on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    location = models.CharField(max_length=LOCATION_MAX_LENGTH, blank=True)
    is_published = models.BooleanField()
    event_start_date = models.DateTimeField()
    event_end_date = models.DateTimeField()
    category = models.ManyToManyField('Category')
    is_online = models.BooleanField()
    url = models.URLField()
    is_verify = models.BooleanField()



class Category(CreatedDateModel):
    name = models.CharField(max_length=CATEGORY_MAX_LENGTH)


class Organizer(CreatedDateModel):
    name = models.CharField(max_length=ORGANIZER_NAME_MAX_LENGTH)
    link = models.URLField()


class Comment(CreatedDateModel):
    text = models.TextField(max_length=COMMENT_MAX_LENGTH)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

