from turtle import setundobuffer
from django.shortcuts import render, redirect
from users.models import Profile
from social_app.models import Post
from .forms import PostForm
from django.contrib.auth.models import User

# Create your views here.

# def base(request):
#     return render(request, 'social_app/base.html')

# def register(request):
#     return render(request, 'social_app/registration.html')

# def index(request):
#     return render(request, 'social_app/index.html')

def add_post(request):
    if request.method == 'GET':
        # do stuff
        form = PostForm()
        form.author = request.user
        return render(request, 'social_app/add_post.html', {'form': form }) 
    elif request.method == 'POST':
        posts = Post.objects.all().order_by('created_on')
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = Profile.objects.get(user=request.user)
            print(request.user)
            new_post.save()
            return redirect('http://127.0.0.1:8000/login/', posts)
