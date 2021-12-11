from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blo')
    title = models.CharField(max_length=264)
    post = models.TextField()
    Image = models.ImageField(upload_to='pics',blank = True)
    Video = models.FileField(upload_to ='vids',blank = True)
    audio = models.FileField(upload_to ='auds',blank = True)
    documents = models.FileField(upload_to ='docs',blank = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('homeblog')

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bol')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='bok')
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('homeblog')
