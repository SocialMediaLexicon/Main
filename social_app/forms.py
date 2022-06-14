from socket import fromshare
from django import forms 
from social_app.models import Post, PostComments

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
        fields = ['post_content', 'media', 'blog_pic', 'post_status']

class PostCommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='')
    class Meta:
        model = PostComments
        fields = ['body',]        