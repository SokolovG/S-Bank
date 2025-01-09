from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path('profile/', views.Profile_view.as_view(), name='profile'),
]