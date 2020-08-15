
# Django
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# Django Rest Framework
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

# Views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-verify/', verify_jwt_token, name='verify_jwt'),

    path('', include(('podcasts.urls', 'podcasts'), namespace='podcasts')),
    path('', include(('users.urls', 'users'), namespace='users'))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
