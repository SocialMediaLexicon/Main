
from django.conf.urls import url
from users import views


app_name = 'users'

urlpatterns = [
    url(r'^logout/$', views.user_logout, name="logout"),
    # url(r'^login/$', views.login, name="login"),
    url(r'^editprofile/$', views.editprofile, name="editprofile"),

    

]