
# Django


# Django REST Framework
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.views import ObtainJSONWebToken

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


class ObtainJSONWebTokenView(ObtainJSONWebToken):
    permission_classes = []

    def get_permissions(self):
        return []


class UserViewSet(RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    lookup_field = 'username'


    @action(methods=['put'], detail=True, permission_classes=[])
    def follow(self, request, *args, **kwargs):
        status_code: int = None
        profile: Profile = request.user.profile

        if self.get_object() not in profile.follows.all() and self.get_object() != request.user:
            profile.follows.add(self.get_object())
            profile.save()
            status_code = status.HTTP_200_OK
        else:
            status_code = status.HTTP_400_BAD_REQUEST
        
        return Response(data=UserModelSerializer(instance=request.user).data, status=status_code)


    @action(methods=['put'], detail=True)
    def unfollow(self, request, *args, **kwargs):
        status_code: int = None
        profile: Profile = request.user.profile

        if self.get_object() in profile.follows.all():
            profile.follows.remove(self.get_object())
            profile.save()
            status_code = status.HTTP_200_OK
        else:
            status_code = status.HTTP_400_BAD_REQUEST
        
        return Response(data=UserModelSerializer(instance=request.user).data, status=status_code)