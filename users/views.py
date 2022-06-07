from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import UserRegisterForm, UserProfilePicForm
# Create your views here.

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserRegisterForm(data=request.POST)
        profile_form = UserProfilePicForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            # if 'profile_pic' in request.FILES:
            #     profile.profile_pic = request.FILES['profile_pic']

            # profile.save()
            image = request.FILES['profile_pic']
            if image:
                filename = FileSystemStorage().save('profile_pics/' + image.name, image)
                profile.profile_pic = filename
            profile.save()
            
            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserRegisterForm()
        profile_form = UserProfilePicForm()

    return render(request, 'users/registration.html', 
                  {'user_form':user_form,
                  'profile_form':profile_form,
                  'registered':registered
                  })


def login(request):
    return render(request, 'users/login.html')