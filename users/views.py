
# Django


# Django REST Framework
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.generics import CreateAPIView

# Models
from django.contrib.auth.models import User
from podcasts.models import Podcast
from users.models import Profile

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
        Profile.objects.create(user=self.user)


class UserViewSet(RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    lookup_field = 'username'