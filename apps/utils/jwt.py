from apps.user.serializers import UserGetSerializer


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserGetSerializer(user, context={'request': request}).data
    }
