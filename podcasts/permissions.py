
# Django REST Framework
from rest_framework import permissions


class IsOwnerObject(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.author