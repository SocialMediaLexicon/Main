from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import UserForm, UserProfileForm, UpdateUserForm
from django.contrib.auth import authenticate, login as dj_login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from django.contrib.auth.models import User
from social_app.models import Post


# Create your views here.

@login_required
def follow_unfollow_profile(request):
    if request.method == 'POST':
        my_profile = Profile.objects.get(user = request.user)
        id = request.POST.get('profile_id')
        obj = Profile.objects.get(id=id)

        if obj.user in my_profile.following.all():
            my_profile.following.remove(obj.user)
            #notify = Notification.objects.filter(sender=request.user, notification_type=2)
            #notify.delete()
        else:
            my_profile.following.add(obj.user)
            #notify = Notification(sender=request.user, user=obj.user, notification_type=2)
            #notify.save()
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('users/all_profiles')


def login(request):
    queryset = Post.objects.filter(post_status=1)
    post_dict = {'post_list' : queryset}
    #user = UserForm()
    #print(user.username, user.password)
    if request.method == 'POST':
        #user = UserForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)
        # print(user)
        if user:
            
            if user.is_active:
                dj_login(request, user)
                return HttpResponseRedirect(reverse(login))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            
            print("Someone tried to login and failed")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("Invalid login details!")
            #return 'bla'

    else:
        return render(request, 'users/user_profile.html', context=post_dict)
     #return render(request, 'users/user_profile.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            image = request.FILES['profile_pic']
            if image:
                filename = FileSystemStorage().save('profile_pics/' + image.name, image)
                profile.profile_pic = filename
            profile.save()
            
            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'users/registration.html', 
                  {'user_form':user_form,
                  'profile_form':profile_form,
                  'registered':registered
                  })


def home(request):
    return render(request, 'users/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(home))


def editprofile(request):
    user = request.user
    userpro =UpdateUserForm(instance=user)
    profile_form = UserProfileForm(instance=request.user.profile)

    if request.method=="POST":
        user_form = UpdateUserForm(data=request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect( 'login')
    return render(request, "users/editprofile.html", {'user_form':userpro, 'profile_form': profile_form})

# def user_login(request):
#     return render(request, 'users/login.html')

class ProfileListView(LoginRequiredMixin,ListView):
    model = Profile
    template_name = "users/all_profiles.html"
    context_object_name = "profiles"

    def get_queryset(self):
        return Profile.objects.all().exclude(user=self.request.user)


class ProfileDetailView(LoginRequiredMixin,DetailView):
    model = Profile
    template_name = "users/user_profile_details.html"
    context_object_name = "profiles"

    def get_queryset(self):
        return Profile.objects.all().exclude(user=self.request.user)

    def get_object(self,**kwargs):
        id = self.kwargs.get("id")
        view_profile = Profile.objects.get(id=id)
        return view_profile

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     view_profile = self.get_object()
    #     my_profile = Profile.objects.get(user=self.request.user)
    #     if view_profile.user in my_profile.following.all():
    #         follow = True
    #     else:
    #         follow = False
    #     context["follow"] = follow