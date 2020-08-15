
# Django
from django.db.models import Q, Count

# Django REST Framework
from rest_framework import serializers

# Models
from django.contrib.auth.models import User
from podcasts.models import Podcast
from users.models import Profile

# Serializers
from podcasts.serializers import TagModelSerializer



class UserPodcastSerializer(serializers.ModelSerializer):

    tags = TagModelSerializer(many=True, read_only=True)

    class Meta:
        model = Podcast
        exclude = ['is_active', 'author']


class FollowerModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']


class ProfileModelSerializer(serializers.ModelSerializer):

    follows = FollowerModelSerializer(many=True, read_only=True)
    followers = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(required=True)
    updated_at = serializers.DateTimeField(required=True)

    class Meta:
        model = Profile
        fields = ['id', 'biography', 'followers', 'follows', 'created_at', 'updated_at']


    def get_followers(self, obj: Profile):
        query = User.objects.filter(profile__follows__in=[obj.user])
        return FollowerModelSerializer(instance=query, many=True).data


class UserModelSerializer(serializers.ModelSerializer):

    profile = ProfileModelSerializer(read_only=True)
    podcasts = UserPodcastSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile', 'podcasts']



class RegisterUserModelSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        read_only_fields = ['id']
        write_only_fields = ['password']


    def create(self, data):
        user = User.objects.create(
            username=data['username'],
            email=data['email']
        )

        user.set_password(data['password'])
        user.save()

        return user


