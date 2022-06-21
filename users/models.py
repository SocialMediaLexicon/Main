from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_online = models.BooleanField(default=False)
    following = models.ManyToManyField(User, related_name="following", blank=True)
    date_of_birth = models.CharField(blank=True,max_length=150)
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics',blank=True, null=True)

    def profile_posts(self):
        return self.user.post_set.all()
        
    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse(' user_profile_details', args=(str(self.id)))


