from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from cloud_storage.models import storage,Image,Video,Audio,Document
class User_login(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password')

class Image_form(ModelForm):
    # Video = forms.FileField(widget=forms.FileInput(attrs={'accept':'video/mp4,video/x-m4v,video/avi,video/mov,video/flv,video/avchd,video/*'}))
    # audio = forms.FileField(widget=forms.FileInput(attrs={'accept':'audio/mpeg,audio/m4a,audio/mp3,audio/wav,audio/*'}))
    # documents = forms.FileField(widget=forms.FileInput(attrs={'accept':'.doc,.docx,.pdf,.html,.htm,.xls,.xlsx,.txt,.ppt,.pptx,.odp,.key'}))
    class Meta():
        model = storage
        fields = ['Image',]

class Video_form(ModelForm):
    Video = forms.FileField(widget=forms.FileInput(attrs={'accept':'video/mp4,video/x-m4v,video/avi,video/mov,video/flv,video/avchd,video/*'}))
    class Meta():
        model = storage
        fields = ['Video',]

class Audio_form(ModelForm):
    audio = forms.FileField(widget=forms.FileInput(attrs={'accept':'audio/mpeg,audio/m4a,audio/mp3,audio/wav,audio/*'}))
    class Meta():
        model = storage
        fields = ['audio',]

class Document_form(ModelForm):
    documents = forms.FileField(widget=forms.FileInput(attrs={'accept':'.doc,.docx,.pdf,.html,.htm,.xls,.xlsx,.txt,.ppt,.pptx,.odp,.key'}))
    class Meta():
        model = storage
        fields = ['documents',]
