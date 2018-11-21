from django.urls import path, include
from . import views

app_name = 'tweetpage'

urlpatterns = [
  path('', views.tweet_page, name='page'),
]