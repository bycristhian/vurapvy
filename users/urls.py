

# Django
from django.urls import path, include

# Django REST Framework
from rest_framework import routers

# Views
from users.views import RegisterUserView, UserViewSet, ObtainJSONWebTokenView


router = routers.SimpleRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('login/', ObtainJSONWebTokenView.as_view(), name='login_user'),
    path('', include(router.urls), name='viewset_users')
]
