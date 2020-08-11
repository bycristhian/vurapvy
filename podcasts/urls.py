
# Django


# Django REST Framework
from rest_framework import routers

# Views
from podcasts.views import PodcastViewSet


router = routers.SimpleRouter()
router.register(r'podcasts', PodcastViewSet)


urlpatterns = router.urls
