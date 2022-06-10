from turtle import setundobuffer
from django.shortcuts import render, redirect
from .forms import PostForm
from users.models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.

def base(request):
    return render(request, 'social_app/base.html')

def register(request):
    return render(request, 'social_app/registration.html')

def index(request):
    return render(request, 'social_app/index.html')
    
    
@login_required
def user_profile(request):
    queryset = Post.objects.filter(status=1)

    post_dict = {'post_list': queryset}
    print(post_dict)
    return render(request, 'users/user_profile.html', context=post_dict)
def add_post(request):
    
    if request.method == 'POST':

        post_form = PostForm(data=request.POST, files=request.FILES)
    
        if post_form.is_valid():

            blogpost = post_form.save(commit=False)

            blogpost.author = request.user

            blogpost.save()

            return redirect('login')

        # else:

        #     print(post_form.error)

    else:

        post_form = PostForm()
    return render(request, 'social_app/add_post.html', {'form': post_form }) 

    # if request.method == 'GET':
    #     if request.user.is_authenticated():
    #         profile = request.user.username
    #         print(profile) 
            # form.author = request.user.username
    # print(form.author)

