from turtle import setundobuffer
from django.shortcuts import render
from .forms import PostForm

# Create your views here.

def base(request):
    return render(request, 'social_app/base.html')

def register(request):
    return render(request, 'social_app/registration.html')

def index(request):
    return render(request, 'social_app/index.html')

def add_post(request):
    if request.method == 'GET':
        # do stuff
        form = PostForm()
        form.author = request.user
        return render(request, 'social_app/add_post.html', {'form': form }) 
    else:
        # request
        return #
