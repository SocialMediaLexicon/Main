from xml.etree.ElementInclude import include
from django.conf.urls import url, include
from users import views
from social_app.views import add_post
from users.views import ProfileListView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'users'

urlpatterns = [
    
    url(r'^logout/$', views.user_logout, name="logout"),
    # url(r'^user/', include('social_app.urls')),
    url(r'^editprofile/$', views.editprofile, name="editprofile"),
    url(r'^all_profiles/', views.ProfileListView.as_view(), name='all_profiles'),
    url(r'^follow/', views.follow_unfollow_profile, name='follow-unfollow'),
    url(r'^person/(?P<id>[0-9]+)/$', views.ProfileDetailView.as_view(), name='user_profile_details'),
 
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)