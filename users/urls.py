

# Django
from django.urls import path, include

# Django REST Framework
from rest_framework import routers

# Views
from users.views import RegisterUserView, UserViewSet


router = routers.SimpleRouter()
router.register(r'users', UserViewSet)

print(router.urls)


urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('', include(router.urls), name='viewset_users')
]
