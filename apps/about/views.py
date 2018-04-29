from rest_framework import viewsets,mixins
from rest_framework.permissions import IsAuthenticated

from about.models import About
from about.serializers import AboutSeializer
from utils.permission import IsOwnerOrReadOnly

class AboutViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):

    def get_permissions(self):
        if self.action == 'retrieve':
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

        return [premission() for premission in permission_classes]

    queryset = About.objects.all()
    serializer_class = AboutSeializer