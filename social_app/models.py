from django.db import models
from users.models import Profile
from django.contrib.auth.models import User

# Create your models here.

reactions = [('0', 'none'),
             ('1', 'like'),
             ('2', 'dislike')
             ]
status = [('1', 'publish'),
          ('2', 'draft')]

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_content = models.TextField(max_length=2000, null=False)
    media = models.FileField(upload_to='post_files',blank=True,null=True)
    likes = models.ManyToManyField(Profile, blank=True, related_name='post_likes')
    dislikes = models.ManyToManyField(Profile, blank=True, related_name='post_dislikes')
    created_on = models.DateTimeField(auto_now_add=True)
    post_status = models.CharField(max_length=7, null=False, choices=status)
    blog_pic = models.ImageField(upload_to="blog_pics", blank=True, null=True)

    def __str__(self):
        return str(self.author)

    @property
    def photo_url(self):
        if self.blog_pic and hasattr(self.blog_pic, 'url'):
            return self.blog_pic.url
    
    
    
    
class PostComments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    comment_content = models.TextField(max_length=500, null=False, blank=False)
    likes = models.ManyToManyField(Profile, blank=True, related_name='comment_likes')
    dislikes = models.ManyToManyField(Profile, blank=True, related_name='comment_dislikes')

    