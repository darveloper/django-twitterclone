from django import forms
from django.contrib.auth.forms import UserCreationForm
from twitteruser.models import CustomUser

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email'
        ]