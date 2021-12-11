from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from blog.models import Blog,Comments
class User_login(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password')

class Com(ModelForm):
    class Meta():
        model = Comments
        fields = ('comment',)

class Normal(ModelForm):
    class Meta():
        model = Blog
        fields = ('title','post')

class Image(ModelForm):
    class Meta():
        model = Blog
        fields = ('title','post','Image')

class Video(ModelForm):
    Video = forms.FileField(widget=forms.FileInput(attrs={'accept':'video/mp4,video/x-m4v,video/avi,video/mov,video/flv,video/avchd,video/*'}))
    class Meta():
        model = Blog
        fields = ('title','post','Video')

class audio(ModelForm):
    audio = forms.FileField(widget=forms.FileInput(attrs={'accept':'audio/mpeg,audio/m4a,audio/mp3,audio/wav,audio/*'}))
    class Meta():
        model = Blog
        fields = ('title','post','audio')

class documents(ModelForm):
    documents = forms.FileField(widget=forms.FileInput(attrs={'accept':'.doc,.docx,.pdf,.html,.htm,.xls,.xlsx,.txt,.ppt,.pptx,.odp,.key'}))
    class Meta():
        model = Blog
        fields = ('title','post','documents')
