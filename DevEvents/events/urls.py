from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework_nested import routers

from api.views import EventViewSet, CommentViewSet


router = DefaultRouter()
comment_router = routers.DefaultRouter()

router.register('events', EventViewSet, basename='event')
comment_router.register('comments', CommentViewSet, basename='post-comments')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(comment_router.urls)),

]