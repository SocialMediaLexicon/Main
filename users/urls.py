from xml.etree.ElementInclude import include
from django.conf.urls import url, include
from users import views
from social_app.views import add_post
from users.views import ProfileListView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'users'

urlpatterns = [
    
    # url(r'^register/$', views.register, name="register"),
    url(r'^logout/$', views.user_logout, name="logout"),
    # url(r'^user/', include('social_app.urls')),
    url(r'^editprofile/$', views.editprofile, name="editprofile"),
    url(r'^all_profiles/', views.ProfileListView.as_view(), name='all_profiles'),
    url(r'^par/(?P<pk>[0-9]+)/$/$', views.ProfileDetailView.as_view(), name='user_profile_details'),
    url(r'^user_profile/$', views.user_profile, name="user_profile"),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)