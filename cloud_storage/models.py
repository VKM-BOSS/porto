from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class storage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='files')
    Image = models.ImageField(upload_to='pics',blank = True)
    Video = models.FileField(upload_to ='vids',blank = True)
    audio = models.FileField(upload_to ='auds',blank = True)
    documents = models.FileField(upload_to ='docs',blank = True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('home')

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='img')
    Image = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('home')

class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vid')
    Video = models.FileField(upload_to ='vids')

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('home')

class Audio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='aud')
    audio = models.FileField(upload_to ='auds')

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('home')

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doc')
    documents = models.FileField(upload_to ='docs')

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('home')
