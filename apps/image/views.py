from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.contrib.auth import get_user_model
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import list_route, detail_route
from rest_framework import status
from rest_framework.settings import api_settings



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