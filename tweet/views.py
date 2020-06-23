from django.shortcuts import render, HttpResponseRedirect, reverse
import re
from .forms import TweetForm
from .models import Tweet
from twitteruser.models import CustomUser
from notification.models import Notification

def notification_alert(tweet):
    mention_pattern = r'([@#][\w_-]+)'
    tag = re.match(mention_pattern, tweet.text)
    if tag:
        tagged_user = CustomUser.objects.get(username=tag.group()[1:])
        Notification.objects.create(
            receiver=tagged_user,
            tweet=tweet
        )

def tweet_view(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.author = CustomUser.objects.get(id=request.user.id)
            tweet.save()
            notification_alert(tweet)
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'generic_form.html', {'form': TweetForm()})

def detail_view(request, id):
    tweet = Tweet.objects.get(id=id)
    return render(request, 'tweet_detail.html', {'tweet': tweet})
