from django.conf.urls import url
from social_app import views
from social_app.views import add_post

app_name = "user"
urlpatterns = [
    url(r'^add_post/', views.add_post, name='add_post'),
    
]
