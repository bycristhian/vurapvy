

# Django REST Framework
from rest_framework import serializers

# Models
from podcasts.models import Tag, Podcast


class TagSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=20, required=True)

    def validate_name(self, name):
        try:
            return Tag.objects.get(name=name)
        except Tag.DoesNotExist:
            raise serializers.ValidationError("The tag {} doesn't exist".format(name))


class TagModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        fields = ['id', 'name', 'created_at', 'updated_at']



class UpdateTagPodcastModelSerializer(serializers.ModelSerializer):

    tags = TagSerializer(many=True)

    class Meta:
        model = Podcast
        fields = ['tags']


    def validate_tags(self, tags):
        return [tag['name'] for tag in tags]


    def update(self, instance: Podcast, validated_data):
        tags = [tag for tag in validated_data['tags'] if tag not in instance.tags.all()]
        instance.tags.add(*tags)
        instance.save()
        return instance







