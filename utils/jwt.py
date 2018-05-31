from django.contrib.auth.signals import user_logged_in

from apps.user.serializers import UserGetSerializer


def jwt_response_payload_handler(token, user=None, request=None):
    """
      jwt 荷载处理
    :param token:
    :param user:
    :param request:
    :return:
    """
    # 这里会发送一个登录的信号
    user_logged_in.send(sender='',user=user,request=request)
    return {
        'token': token,
        'user': UserGetSerializer(user, context={'request': request}).data
    }
