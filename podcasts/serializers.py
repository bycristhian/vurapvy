
# Django


# Django REST Framework
from rest_framework import serializers

# Serializers
from users.serializers import UserModelSerializer

# Models
from podcasts.models import Podcast, Tag
from django.contrib.auth.models import User




class TagModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        fields = ['id', 'name', 'created_at', 'updated_at']


class PodcastModelSerializer(serializers.ModelSerializer):
    
    author = UserModelSerializer(read_only=True)
    tags = TagModelSerializer(many=True, read_only=True)

    class Meta:
        model = Podcast
        fields = ['id', 'name', 'description', 'author', 'tags', 'image', 'audio', 'created_at', 'updated_at']



class CreatePodcastModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Podcast
        fields = ['name', 'description', 'image', 'audio']


    def save(self, author: User):
        data = self.validated_data
        data['author'] = author

        return Podcast.objects.create(**data)
