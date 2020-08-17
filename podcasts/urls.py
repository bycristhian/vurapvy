
# Django


# Django REST Framework
from rest_framework import routers

# Views
from podcasts.views import PodcastViewSet, TagViewSet


router = routers.SimpleRouter()
router.register(r'podcasts', PodcastViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = router.urls
