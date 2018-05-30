from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication

from utils.permission import IsOwnerOrReadOnly
from image.models import Image
from image.serializers import BlogListImgSerializer


class BlogImgViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    '''
    create:
    创建图片
    '''

    authentication_classes = (SessionAuthentication, JSONWebTokenAuthentication)
    queryset = Image.objects.all()
    serializer_class = BlogListImgSerializer

    parser_classes = (MultiPartParser, FileUploadParser,)

    def get_permissions(self):
        permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
        return [premission() for premission in permission_classes]