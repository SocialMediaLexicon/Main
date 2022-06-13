from django.contrib import admin
from .models import Notification

# Register your models here.
from .models import Profile

admin.site.register(Profile)
admin.site.register(Notification)