from tracardi_python_sdk.errors import ResponseError, AuthenticationError


class Dispatcher:

    def __init__(self, url):
        self.url = url
        self.token = ""

    def _error(self, body, status):

        if status == 401:
            raise AuthenticationError("Not authenticated.")

        if status == 404:
            raise ResponseError("API endpoint {} does not exist.".format(self.url), status=status)

        if 'detail' in body:
            if isinstance(body['detail'], dict):
                errors = []
                for error in body['detail']:
                    errors.append(" Location: {}, Message: {}".format(error['loc'], error['msg']))
                raise ResponseError(",".join(errors), status=status)
            else:
                raise ResponseError(body['detail'], status=status)

        raise ResponseError("API did not return 200 OK status.", status=status)
