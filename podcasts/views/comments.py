
# Django
from django.http.response import Http404

# Django REST Framework
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin

# Models
from podcasts.models import Podcast

# Serializers
from podcasts.serializers import CreateCommetModelSerializer, PodcastModelSerializer



class CommentViewSet(CreateModelMixin, GenericViewSet):
    queryset = Podcast.objects.all()
    serializer_class = CreateCommetModelSerializer

    def dispatch(self, request, *args, **kwargs):
        try:
            self.podcast = Podcast.objects.get(pk=kwargs['pk_podcast'])
        except Podcast.DoesNotExist:
            raise Http404("The podcast doesn't exists")

        return super().dispatch(request, *args, **kwargs)


    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = PodcastModelSerializer(instance=self.podcast).data

        return response

    def perform_create(self, serializer):
        serializer.save(self.podcast, self.request.user)