from xml.etree.ElementInclude import include
from django.conf.urls import url, include
from users import views
from social_app.views import add_post


#app_name = 'users'

urlpatterns = [
    url(r'^register/$', views.register, name="register"),
    url(r'^logout/$', views.user_logout, name="logout"),
    url(r'^login/$', views.user_login, name="user_login"),
    url(r'^user/', include('social_app.urls')),
    url(r'^editprofile/$', views.editprofile, name="editprofile"),

]