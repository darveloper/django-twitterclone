from django.urls import path
from twitteruser.views import (
    index, user_view, follow_view, unfollow_view
)

urlpatterns = [
    path('', index, name='home'),
    path('user/<int:user_id>', user_view),
    path('follow/<int:user_id>', follow_view),
    path('unfollow/<int:user_id>', unfollow_view),
]
