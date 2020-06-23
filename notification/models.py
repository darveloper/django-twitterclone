from django.db import models
from twitteruser.models import CustomUser
from tweet.models import Tweet

class Notification(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE)