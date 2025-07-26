from django.urls import path
from . import views  # ✅ importing your views module

urlpatterns = [
    path('tweets/new/', views.tweet_new, name='tweet_new'),
    path('', views.tweet_list, name='home'),
]
