from django.conf import settings
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
import uuid

from utils.auth.auth_github import AuthGithub
from oauth.models import OAuth
from user.models import User


class OAuthViewSet(viewsets.GenericViewSet):

    @action(methods=['get'], detail=False)
    def github_login(self, request, pk=None):
        auth = AuthGithub(settings.GITHUB_APP_ID, settings.GITHUB_KEY, settings.GITHUB_CALLBACK_URL)
        url = auth.get_auth_url()
        return HttpResponseRedirect(url)

    @action(methods=['get'], detail=False)
    def github_check(self, request, pk=None):
        code = request.query_params['code']
        auth = AuthGithub(settings.GITHUB_APP_ID, settings.GITHUB_KEY, settings.GITHUB_CALLBACK_URL)
        token = auth.get_access_token(code)
        user_info = auth.get_user_info()
        nickname = user_info.get('login', '')
        image_url = user_info.get('avatar_url', '')
        open_id = str(auth.openid)
        signature = user_info.get('bio', '')
        if not signature:
            signature = "无个性签名"
        sex = '3'

        oauth = OAuth.objects.filter(openid=open_id,type='1')
        if oauth:
            return Response(data={'aaa':'ff'})
        else:
            user =User.objects.create(username=nickname,desc=signature,password=uuid.uuid1(),sex=sex)
            user.img_download(image_url,nickname)
        return Response()
