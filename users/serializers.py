
# Django


# Django REST Framework
from rest_framework import serializers

# Models
from django.contrib.auth.models import User


class UserModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email']