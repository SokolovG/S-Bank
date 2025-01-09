from django.db import models
from django.contrib.auth.models import AbstractUser

from constants import MAX_LENGTH, MAX_LENGTH_TEXT


class CreatedDateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class User(AbstractUser):
    username = models.CharField(max_length=MAX_LENGTH, unique=True)
    first_name = models.CharField(max_length=MAX_LENGTH)
    last_name = models.CharField(max_length=MAX_LENGTH)
    email = models.EmailField(max_length=MAX_LENGTH, unique=True)
    location = models.CharField(max_length=30, blank=True)
    interested_technologies = models.CharField(max_length=100, blank=True)


    def __str__(self):
        return self.username

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'.strip()


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
