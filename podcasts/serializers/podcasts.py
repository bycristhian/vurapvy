
# Django Rest Framework
from rest_framework import serializers
from django.core.files.temp import TemporaryFile

# Serializers
from users.serializers import UserModelSerializer
from podcasts.serializers import TagModelSerializer

# Models 
from podcasts.models import Podcast
from django.contrib.auth.models import User

from mutagen.mp3 import MP3


class PodcastModelSerializer(serializers.ModelSerializer):
    
    author = UserModelSerializer(read_only=True)
    tags = TagModelSerializer(many=True, read_only=True)

    class Meta:
        model = Podcast
        exclude = ['is_active']



class CreatePodcastModelSerializer(serializers.ModelSerializer):

    tags = TagModelSerializer(many=True, read_only=True)

    class Meta:
        model = Podcast
        fields = ['id', 'name', 'description', 'image', 'audio', 'tags', 'created_at', 'updated_at']
        read_only_fields = ['id', 'tags', 'created_at', 'updated_at']


    def validate_audio(self, data: TemporaryFile):
        try:
            audio = MP3(data.file.name)
            if int(audio.info.length) >= 3600:
                raise serializers.ValidationError("The podcast's audio can't be greater to 00:59:59")
        except AttributeError:
            raise serializers.ValidationError("The podcast's audio just can be .MP3")

        return data


    def save(self, author: User):
        data = self.validated_data
        data['author'] = author

        return Podcast.objects.create(**data)