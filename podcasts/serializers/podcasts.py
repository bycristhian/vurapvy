
# Django Rest Framework
from rest_framework import serializers

# Serializers
from users.serializers import UserModelSerializer
from podcasts.serializers import TagModelSerializer

# Models 
from podcasts.models import Podcast
from django.contrib.auth.models import User


class PodcastModelSerializer(serializers.ModelSerializer):
    
    author = UserModelSerializer(read_only=True)
    tags = TagModelSerializer(many=True, read_only=True)

    class Meta:
        model = Podcast
        exclude = ['is_active']



class CreatePodcastModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Podcast
        fields = ['name', 'description', 'image', 'audio']


    def save(self, author: User):
        data = self.validated_data
        data['author'] = author

        return Podcast.objects.create(**data)