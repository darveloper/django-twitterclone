from django.db import models
from django.utils import timezone
from twitteruser.models import CustomUser

class Tweet(models.Model):
    author = models.ForeignKey(CustomUser, default=None, on_delete=models.CASCADE)
    text = models.CharField(max_length=140)
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
    