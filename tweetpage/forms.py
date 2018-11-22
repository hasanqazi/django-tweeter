from django import forms
from . import models

class CreateTweet(forms.ModelForm):
    class Meta:
        model = models.Tweet
        fields = ['body', 'slug']