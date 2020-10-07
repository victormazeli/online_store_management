from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    is_customer = forms.BooleanField()

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

class LoginForm():
    class Meta:
        model = User
        fields = ('email', 'password1')