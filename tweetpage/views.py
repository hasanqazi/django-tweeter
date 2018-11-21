from django.shortcuts import render
from .models import Tweet

# Create your views here.
def tweet_page(request):
  tweets = Tweet.objects.all().order_by('date')
  return render(request, 'tweetpage/tweet_page.html')