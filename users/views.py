from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User


class Profile_view(LoginRequiredMixin, DetailView):
    model = User
