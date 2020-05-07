from .models import UserProfilePic
from django import forms
from django.contrib.auth.models import User


class User_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['first_name', 'last_name','email', 'username', 'password']


class ProfilePicForm(forms.ModelForm):
    class Meta:
        model = UserProfilePic
        fields = ['profile_pic']


