

# Django
from django.urls import path

# Views
from users.views import RegisterUserView


urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register_user')
]
