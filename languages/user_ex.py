from flask import Response
class APIException(Exception):
    def __init__(self, status=200, success=False, message=''):
        super().__init__()
        self.message = message
        self.status = status
        self.success = success

    def to_resp(self):
        return Response({}, status=self.status, message=self.message, success=self.success)
