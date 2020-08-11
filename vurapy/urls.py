
# Django
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# Django Rest Framework
from rest_framework_jwt.views import obtain_jwt_token

# Views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', obtain_jwt_token, name='obtain_jwt'),
    path('', include(('podcasts.urls', 'podcasts'), namespace='podcasts')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
