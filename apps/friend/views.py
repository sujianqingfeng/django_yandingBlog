from rest_framework import mixins, viewsets
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from friend.serializers import FriendCreateSerializer, FriendUpdateSerializer
from friend.models import Friend
from utils.permission import IsOwnerOrReadOnly


class FriendViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):

    def get_queryset(self):
        # if self.action == 'update' or self.action == 'partial_update':
        #     return Friend.objects.get(id=self.kwargs['pk'])

        if self.action == 'links':
            return Friend.objects.filter(is_delete=False)
        return Friend.objects.all()

    def get_serializer_class(self):

        if self.action == 'create':
            return FriendCreateSerializer
        elif self.action == 'update' or self.action == 'partial_update':
            return FriendUpdateSerializer

        return FriendCreateSerializer

    def get_permissions(self):
        if self.action == 'links':
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

        return [premission() for premission in permission_classes]

    @detail_route(methods=['get'])
    def links(self, request, pk=None):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
