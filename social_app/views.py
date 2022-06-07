from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, 'social_app/base.html')

def register(request):
    return render(request, 'social_app/registration.html')

def index(request):
    return render(request, 'social_app/index.html')