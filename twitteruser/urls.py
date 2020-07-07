from django.urls import path
from twitteruser.views import (
    index, user_view, follow_view, unfollow_view, search_view
)
from authentication.urls import urlpatterns as authentication_urls

urlpatterns = [
    path('', index, name='home'),
    path('user/<int:user_id>', user_view),
    path('search/', search_view, name='search'),
    path('follow/<int:user_id>', follow_view),
    path('unfollow/<int:user_id>', unfollow_view),
]

urlpatterns += authentication_urls
