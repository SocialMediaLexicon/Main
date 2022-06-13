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
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from social_app import views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', user_views.home, name='home'), 
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('users.urls')),
    url(r'^register/$', user_views.register, name='register'),
    url(r'^logout/$', user_views.user_logout, name="logout"),
    url(r'^login/$', user_views.login, name="login"),
    url(r'^user/', include('social_app.urls')),
    #url(r'^user_profile/$', user_views.user_profile, name="user_profile"),
    #url(r'^editprofile/$', user_views.editprofile, name="editprofile"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
