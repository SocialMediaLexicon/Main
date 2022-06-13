from django.contrib import admin
from friend.models import FriendList, FriendRequest

# Register your models here.


admin.site.register(FriendList)
admin.site.register(FriendRequest)