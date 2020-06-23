from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    text = forms.CharField(max_length=140)
    class Meta:
        model = Tweet
        fields = [
            'text'
        ]