from django.urls import path
from .views import (
    tweet_view, detail_view
)

urlpatterns = [
    path('add/', tweet_view),
    path('tweet/<int:id>', detail_view)
]
