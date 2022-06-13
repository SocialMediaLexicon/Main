from socket import fromshare
from django import forms 
from social_app.models import Post

class PostForm(forms.ModelForm):
    
    post_content = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': 5,
            'placeholder': 'Share with us...'
        })
    )
    
    class Meta:
        model = Post
        exclude = ['author']
        fields = ['post_content', 'media', 'blog_pic', 'post_status']
        