# tweets/views.py
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.shortcuts import render

from .models import Tweet

class TweetListView(ListView):
    model = Tweet
    template_name = 'home.html'

class TweetCreateView(CreateView):
    model = Tweet
    template_name = 'tweet_new.html'
    fields = ['user', 'body']

    def get_success_url(self):
        return reverse('home')

def about_page(request):
    return render(request, 'about.html')
