from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, 'social_app/base.html')

def register(request):
    return render(request, 'users/registration.html')

def login(request):
    return render(request, 'users/login.html')