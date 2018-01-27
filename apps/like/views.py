from rest_framework import viewsets
from rest_framework import mixins
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication

from like.models import Like
from like.serializers import LikeCreateSerializer,LikeDetailSerializer
from utils.permission import IsOwnerOrReadOnly


class LikeViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin,mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
    list:
    收藏列表

    create:
    添加收藏

    ｄetele:
    删除收藏
    '''

    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly,)
    authentication_classes = (SessionAuthentication,JSONWebTokenAuthentication)

    def get_queryset(self):
        return Like.objects.all(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return LikeDetailSerializer
        else:
            return LikeCreateSerializer