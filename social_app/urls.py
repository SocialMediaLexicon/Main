from django.conf.urls import url
from social_app.views import add_post

urlpatterns = [
    url(r'add_post/', add_post),
    
]
