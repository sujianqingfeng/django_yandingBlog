from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['desc'] = {}

        if 'detail' in response.data.keys():

            response.data['desc'] = response.data['detail']
            # response.data['data'] = None
            del response.data['detail']
        else:
            pass

        response.data['code'] = response.status_code

    return response
