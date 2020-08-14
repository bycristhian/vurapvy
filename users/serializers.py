
# Django


# Django REST Framework
from rest_framework import serializers

# Models
from django.contrib.auth.models import User
from podcasts.models import Podcast

# Serializers
from podcasts.serializers import TagModelSerializer



class UserPodcastSerializer(serializers.ModelSerializer):

    tags = TagModelSerializer(many=True, read_only=True)

    class Meta:
        model = Podcast
        exclude = ['is_active', 'author']



class UserModelSerializer(serializers.ModelSerializer):

    podcasts = UserPodcastSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'podcasts']



class RegisterUserModelSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        read_only_fields = ['id']