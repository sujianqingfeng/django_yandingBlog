#!/usr/bin/env python
# encoding: utf-8


from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from rest_framework.mixins import CreateModelMixin
from rest_framework import viewsets


from .serializers import UserRegisterSerializer


User = get_user_model()

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(phone=username))

            if user.check_password(password):
                return user
        except Exception as e:
            return None


class UserViewset(CreateModelMixin,viewsets.GenericViewSet):
    serializer_class = UserRegisterSerializer
