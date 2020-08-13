
# Django


# Django REST Framework
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.generics import CreateAPIView

# Models
from django.contrib.auth.models import User

# Serializers
from users.serializers import RegisterUserModelSerializer


class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = []
    serializer_class = RegisterUserModelSerializer