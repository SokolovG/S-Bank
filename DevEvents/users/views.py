from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics

from .models import User


class Profile_view(LoginRequiredMixin, generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = ''

