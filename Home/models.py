from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class mail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sub')
    frommail = models.CharField(max_length=264)
    tomail = models.CharField(max_length=264)
    subject = models.CharField(max_length=264)
    content = models.TextField()

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('homemail')
