
# Django
from django.shortcuts import render

# Django REST Framework
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Serializers
from .serializers import CreatePodcastModelSerializer, PodcastModelSerializer

# Models
from podcasts.models import Podcast



class PodcastViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    model = Podcast
    queryset = Podcast.objects.all()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        serializer = PodcastModelSerializer(instance=self.podcast)
        response.data = serializer.data

        return response

    def perform_create(self, serializer):
        self.podcast = serializer.save(self.request.user)

    def get_serializer_class(self):
        serializer = None
        if self.action == 'create':
            serializer = CreatePodcastModelSerializer
        elif self.action == 'list':
            serializer = PodcastModelSerializer

        return serializer



