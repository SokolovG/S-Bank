from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics

from .models import User


class ProfileView(LoginRequiredMixin, generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = ''

