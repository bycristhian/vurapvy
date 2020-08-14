
# Django
from django.db import models

# Models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True, blank=False, null=False)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Podcast(models.Model):
    name = models.CharField(max_length=35)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='podcasts')
    tags = models.ManyToManyField(Tag, related_name='podcasts_tag')

    image = models.ImageField(upload_to='podcasts_images', blank=False, null=False)
    audio = models.FileField(upload_to='podcasts_audio', blank=False, null=False)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)