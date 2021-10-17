# from django.forms import fields
from instagram.models import Profile,Image,Comment
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UpdateuserForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class UpdateprofileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic','bio','user')

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ("image","caption")

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','body')