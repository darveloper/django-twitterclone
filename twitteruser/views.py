from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from tweet.models import Tweet
from .models import CustomUser
from notification.models import Notification

@login_required(login_url='/login')
def index(request):
    following = request.user.following.all()
    tweets = Tweet.objects.filter(author__in=following).order_by("-post_date")
    notifications = Notification.objects.filter(receiver=request.user)
    return render(request, 'index.html', {'tweets': tweets, 'notifications': notifications})

def user_view(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    tweets = Tweet.objects.filter(author=user)
    logged_in_user = CustomUser.objects.get(id=request.user.id)
    is_following = logged_in_user.following.filter(id=user_id).exists()
    return render(request, 'userpage.html', {
        'user': user,
        'tweets': tweets,
        'is_following': is_following
    })

def follow_view(request, user_id):
    user_follow = CustomUser.objects.get(id=user_id)
    logged_in_user = CustomUser.objects.get(id=request.user.id)
    logged_in_user.following.add(user_follow)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def unfollow_view(request, user_id):
    user_unfollow = CustomUser.objects.get(id=user_id)
    logged_in_user = CustomUser.objects.get(id=request.user.id)
    logged_in_user.following.remove(user_unfollow)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))