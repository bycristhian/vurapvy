
# Django


# Django REST Framework
from rest_framework import routers

# Views
from podcasts.views import PodcastViewSet, TagViewSet, CommentViewSet


router = routers.SimpleRouter()
router.register(r'podcasts', PodcastViewSet)
router.register(r'tags', TagViewSet)
router.register(r'podcasts/(?P<pk_podcast>[^/.]+)/comments', CommentViewSet)

urlpatterns = router.urls
