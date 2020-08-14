
# Django
from django.db import models

# Models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    biography = models.CharField(max_length=160, blank=True, null=True)
    follows = models.ManyToManyField(User, related_name='follows_user')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} by {}".format(self.biography, self.user)

