from django.db import models
from django.contrib.auth.models import User
# Create your models here.


""" Model for User Profile """

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_online = models.BooleanField(default=False)
    following = models.ManyToManyField(User, related_name="following", blank=True)
    date_of_birth = models.CharField(blank=True,max_length=150)
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics',blank=True, null=True)

    def __str__(self):
        return self.user.username
