# pages/urls.py
from django.urls import path
from .views import homePageView, firstRoute, post

urlpatterns = [
    path("", homePageView, name="home"),
    path('first', firstRoute, name='first'),
    path('post', post, name='post')
]
