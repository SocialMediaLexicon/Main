from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_online = models.BooleanField(default=False)
    friends = models.ManyToManyField(User, related_name='my_friends', blank=True)
    bio = models.CharField(default="",blank=True,null=True,max_length=350)
    following = models.ManyToManyField(User, related_name="following", blank=True)
    date_of_birth = models.CharField(blank=True,max_length=150)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics',blank=True, null=True)

    def profile_posts(self):
        return self.user.post_set.all()
        
    def get_friends_no(self):
        return self.friends.all().count()

    def get_friends(self):
        return self.friends.all()

    def __str__(self):
        return '%s Profile' %(self.user.username)

    def get_absolute_url(self):
        return reverse(' user_profile_details', args=(str(self.id)))


STATUS_CHOICES = (
    ('send','send'),
    ('accepted','accepted')
)

class Relationship(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='friend_sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='friend_receiver')
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"