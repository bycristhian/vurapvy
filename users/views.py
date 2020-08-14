
# Django


# Django REST Framework
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

# Models
from django.contrib.auth.models import User
from podcasts.models import Podcast

# Serializers
from users.serializers import RegisterUserModelSerializer, UserModelSerializer


class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = []
    serializer_class = RegisterUserModelSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = UserModelSerializer(instance=self.user).data
        return response

    def perform_create(self, serializer):
        self.user = serializer.save()


class UserViewSet(RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    lookup_field = 'username'