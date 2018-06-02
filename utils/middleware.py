from .request import judge_pc_or_mobile


class JudgePcOrMobileMiddleware(object):
    """
    判断客户端设备的中间件
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ua = request.META.get('HTTP_USER_AGENT')
        is_mobile = judge_pc_or_mobile(ua)
        request.META['IS_MOBILE'] = is_mobile
        response = self.get_response(request)

        return response
