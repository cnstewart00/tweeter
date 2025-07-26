# tweets/views.py
from django.shortcuts import render, redirect
from .models import Tweet  # only if you're using a Tweet model
from .forms import TweetForm  # only if you have a form defined

# Show a list of tweets
def tweet_list(request):
    tweets = Tweet.objects.all()  # assumes you have a Tweet model
    return render(request, 'tweets/tweet_list.html', {'tweets': tweets})

# Handle tweet creation
def tweet_new(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TweetForm()
    return render(request, 'tweets/tweet_form.html', {'form': form})
