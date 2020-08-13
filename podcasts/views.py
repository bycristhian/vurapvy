
# Django
from django.shortcuts import render

# Django REST Framework
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

# Serializers
from .serializers import (CreatePodcastModelSerializer, PodcastModelSerializer, UpdateTagPodcastModelSerializer)

# Permissions
from podcasts.permissions import IsOwnerObject

# Models
from podcasts.models import Podcast



class PodcastViewSet(CreateModelMixin, ListModelMixin, UpdateModelMixin, 
                     DestroyModelMixin, GenericViewSet):
    model = Podcast
    queryset = Podcast.objects.filter(is_active=True)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        serializer = PodcastModelSerializer(instance=self.podcast)
        response.data = serializer.data

        return response

    def destroy(self, request, *args, **kwargs):
        podcast: Podcast = self.get_object()
        podcast.is_active = False
        podcast.save()

        user_podcasts = self.queryset.filter(author=self.request.user)
        serializer = PodcastModelSerializer(instance=user_podcasts, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        self.podcast = serializer.save(self.request.user)

    def get_serializer_class(self):

        serializer = None
        if self.action == 'create':
            serializer = CreatePodcastModelSerializer
        elif self.action == 'list':
            serializer = PodcastModelSerializer

        return serializer


    def get_permissions(self):
        permissions = super().get_permissions()
        if self.action == 'destroy' or self.action == 'update':
            permissions.append(IsOwnerObject())
        return permissions


    @action(detail=True, methods=['put'], permission_classes=[IsOwnerObject])
    def add_tags(self, request, *args, **kwargs):
        serializer = UpdateTagPodcastModelSerializer(instance=self.get_object(), data=request.data)
        serializer.is_valid(raise_exception=True)
        
        self.update_tags(self.get_object(), serializer.validated_data['tags'], 'add')

        return Response(data=PodcastModelSerializer(instance=self.get_object()).data, status=status.HTTP_200_OK)


    @action(detail=True, methods=['put'], permission_classes=[IsOwnerObject])
    def remove_tags(self, request, *args, **kwargs):
        serializer = UpdateTagPodcastModelSerializer(instance=self.get_object(), data=request.data)
        serializer.is_valid(raise_exception=True)

        self.update_tags(self.get_object(), serializer.validated_data['tags'], 'remove')

        return Response(data=PodcastModelSerializer(instance=self.get_object()).data, status=status.HTTP_200_OK)


    def update_tags(self, instance: Podcast, tags, action: str):
        if action == 'add':
            data = [tag for tag in tags if tag not in instance.tags.all()]
            instance.tags.add(*data)
            
        elif action == 'remove':
            data = [tag for tag in tags if tag in instance.tags.all()]
            instance.tags.remove(*data)

        instance.save()
        return instance


