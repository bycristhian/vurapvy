
# Django REST Framework
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

# Models
from podcasts.models import Tag

# Serializers
from podcasts.serializers import TagModelSerializer


class TagViewSet(ListModelMixin, GenericViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagModelSerializer