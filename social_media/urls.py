"""social_media URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^social_app/', include('social_appurls'))
"""
from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from social_app import views
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   
    path('admin/', admin.site.urls),

    path('accounts/', include('allauth.urls')),

    path('', include('social_app.urls', namespace='social_app')),
    path('user/', include('users.urls', namespace='users')),
    path('notifications/', include('notification.urls', namespace='notification')),
    path('friend/', include('friend.urls', namespace='friend')),
    #path('chats/', include('chat.urls', namespace='chat')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


