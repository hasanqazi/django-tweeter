from django.shortcuts import render, redirect
from .models import Tweet
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def tweet_page(request):
  tweets = Tweet.objects.all().order_by('date')
  return render(request, 'tweetpage/tweet_page.html',{'tweets':tweets})

def create_tweet(request):
  if request.method == 'POST':
    form = forms.CreateTweet(request.POST)
    if form.is_valid():
      instance = form.save(commit=False)
      instance.author = request.user
      instance.save()
      return redirect('tweetpage:page')
  else:
    form = forms.CreateTweet()
  return render(request, 'tweetpage/tweet_create.html', {'form':form})