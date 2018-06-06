import uuid

from django.conf import settings
from django.contrib import auth
from django.http import HttpResponseRedirect
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings

from oauth.models import OAuth
from user.models import User
from user.serializers import UserLoginOrRegisterSerializer
from utils.auth.auth_github import AuthGithub
from utils.jwt import generate_response, generate_token

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER


class OAuthViewSet(viewsets.GenericViewSet):
    serializer_class = UserLoginOrRegisterSerializer
    authentication_classes = ()

    @action(methods=['get'], detail=False)
    def github_login(self, request, pk=None):
        """
        跳转github认证url
        """
        auth = AuthGithub(settings.GITHUB_APP_ID, settings.GITHUB_KEY, settings.GITHUB_CALLBACK_URL)
        url = auth.get_auth_url()
        return HttpResponseRedirect(url)

    @action(methods=['get'], detail=False)
    def pc_github_check(self, request, pk=None):
        return self.github_check(request, is_pc=True)

    @action(methods=['get'], detail=False)
    def mobile_github_check(self, request, pk=None):
        return self.github_check(request, is_pc=False)

    @action(methods=['post'], detail=False)
    def pc_login(self, request, pk=None):
        return self.login(request, is_pc=True)

    @action(methods=['post'], detail=False)
    def moblie_login(self, request, pk=None):
        return self.login(request, is_pc=False)

    @action(methods=['post'], detail=False)
    def pc_register(self, request, pk=None):
        return self.register(request, is_pc=True)

    @action(methods=['post'], detail=False)
    def mobile_register(self, request, pk=None):
        return self.register(request, is_pc=False)

    @staticmethod
    def github_check_before(request):
        """
        github check 之前执行
        """
        code = request.query_params['code']
        auth = AuthGithub(settings.GITHUB_APP_ID, settings.GITHUB_KEY, settings.GITHUB_CALLBACK_URL)
        auth.get_access_token(code)
        user_info = auth.get_user_info()
        nickname = user_info.get('login', '')
        image_url = user_info.get('avatar_url', '')
        open_id = str(auth.openid)
        signature = user_info.get('bio', '')
        if not signature:
            signature = "无个性签名"
        sex = '3'

        oauth = OAuth.objects.get(openid=open_id, type='1')
        return oauth, nickname, image_url, signature, sex, open_id

    def github_check(self, request, is_pc):
        """
        github认证成功后，进行校验
        """
        oauth, nickname, image_url, signature, sex, open_id = self.github_check_before(request)
        if oauth:
            user = oauth.user
            return self.custom_response(request, user, is_pc)
        else:
            user = User.objects.create(username=nickname, desc=signature, password=uuid.uuid1(), sex=sex)
            user.img_download(image_url, nickname)
            user.save()

            instance = OAuth.objects.create(user=user, openid=open_id, type='1')
            instance.save()
            return self.custom_response(request, user, is_pc)

    def login(self, request, is_pc):
        """
        登陆接口 根据不同的客户端返回不同的数据
        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            return self.custom_response(request, user, is_pc)
        else:
            return Response({'detail': '用户不存在'}, status=status.HTTP_400_BAD_REQUEST)

    def register(self, request, is_pc):
        """
        注册接口
        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        user = User.objects.filter(username=username)

        if user:
            return Response({'detail': '用户存在'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            user = serializer.save()
            return self.custom_response(request, user, is_pc)

    @staticmethod
    def custom_response(request, user, is_ps=False):
        if user is not None and user.is_active:
            if is_ps:
                auth.login(request, user)
                return Response(status=status.HTTP_200_OK)
            else:
                token = generate_token(user)
                response = generate_response(token, user, request)
                return response
