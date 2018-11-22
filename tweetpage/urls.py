from django.urls import path, include
from . import views
from django.conf.urls.static import static

app_name = 'tweetpage'

urlpatterns = [
  path('', views.tweet_page, name='page'),
  path('create/', views.create_tweet, name='create')
]