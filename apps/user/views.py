#!/usr/bin/env python
# encoding: utf-8


from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication


from .serializers import UserRegisterSerializer,UserSerializer


User = get_user_model()

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(phone=username))

            if user.check_password(password):
                return user
        except Exception as e:
            return None


class UserViewset(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    '''
    create:
    注册用户

    read:
    得到用户信息

    update:
    修改用户

    partial_update:
    部分修改
    '''

    queryset = User.objects.all()
    authentication_classes = (SessionAuthentication, JSONWebTokenAuthentication)

    def get_object(self):
        return self.request.user


    def get_permissions(self):
        if self.action == 'create':
            return []
        else:
            return [permissions.IsAuthenticated()]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegisterSerializer
        else:
            return UserSerializer