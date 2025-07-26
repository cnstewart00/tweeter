# tweets/urls.py
from django.urls import path
from .views import TweetListView, TweetCreateView, about_page

urlpatterns = [
    path('tweets/new/', TweetCreateView.as_view(), name='tweet_new'),
    path('', TweetListView.as_view(), name='home'),
    path('about/', about_page, name='about'),
]
