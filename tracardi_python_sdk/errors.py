class ResponseError(Exception):

    def __init__(self, *args, **kwargs):
        self.status = kwargs['status'] if 'status' in kwargs else None


class AuthenticationError(Exception):
    pass


class UnknownError(Exception):
    pass
