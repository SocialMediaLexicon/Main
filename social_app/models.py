from django.db import models
from users.models import Profile
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.

reactions = [('0', 'none'),
             ('1', 'like'),
             ('2', 'dislike')
             ]
status = [('1', 'publish'),
          ('2', 'draft')]

class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    post_status = models.CharField(max_length=7, null=False, choices=status)
    media = models.FileField(upload_to='post_files',blank=True,null=True)
    likes = models.ManyToManyField(User, blank=True, related_name='post_likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='post_dislikes')
    saves = models.ManyToManyField(User, related_name="blog_save", blank=True)
    blog_pic = models.ImageField(upload_to="blog_pics", blank=True, null=True)

    def total_likes(self):
        return self.likes.count()

    def total_saves(self):
        return self.saves.count()

    def __str__(self):
        return self.title

    @property
    def photo_url(self):
        if self.blog_pic and hasattr(self.blog_pic, 'url'):
            return self.blog_pic.url

    def get_absolute_url(self):
        return reverse('social_app:post-detail', kwargs={"pk":self.pk})
    
class PostComments(models.Model):
    post = models.ForeignKey(Post, related_name="comments" , on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=200)
    likes = models.ManyToManyField(User, blank=True, related_name='comment_likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='comment_dislikes')
    reply = models.ForeignKey('self', null=True, related_name="replies", on_delete=models.CASCADE)

    def total_clikes(self):
        return self.likes.count()

    def __str__(self):
        return '%s - %s - %s' %(self.post.title, self.name, self.id)

    def get_absolute_url(self):
        return reverse('social_app:post-detail', kwargs={"pk":self.pk})

