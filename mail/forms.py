from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
class User_login(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password')
