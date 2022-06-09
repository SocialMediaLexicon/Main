from django.contrib import admin
from social_app.models import Post, PostComments

# Register your models here.
admin.site.register(Post)
admin.site.register(PostComments)