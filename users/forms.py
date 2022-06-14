from django import forms
from django.contrib.auth.models import User
from .models import Profile
from PIL import Image

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    email = forms.EmailField()
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


class UpdateUserForm(forms.ModelForm): 

    email = forms.EmailField()
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
class UserProfileForm(forms.ModelForm):
    class Meta():
        model = Profile
        fields = ['profile_pic', 'date_of_birth']

class ProfileUpdateForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height = forms.FloatField(widget=forms.HiddenInput(), required=False)

    profile_pic = forms.ImageField(label=('Image'), error_messages = {'invalid':("Image files only")}, widget=forms.FileInput, required=False)
    class Meta:
        model = Profile
        fields = ['bio','date_of_birth','profile_pic',]


    """Saving Cropped Image"""
    def save(self,*args,**kwargs):
        img = super(ProfileUpdateForm, self).save(*args, **kwargs)

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        if x and y and w and h:
            image = Image.open(img.image)
            cropped_image = image.crop((x, y, w+x, h+y))
            resized_image = cropped_image.resize((300, 300), Image.ANTIALIAS)
            resized_image.save(img.image.path)

        return img