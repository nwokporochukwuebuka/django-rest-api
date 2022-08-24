from django.conf import settings
import jwt
from rest_framework.authentication import BaseAuthentication
from user.models import CustomUser
from datetime import datetime

class Authentication(BaseAuthentication):

    def authenticate(self, request):
        data = self.validate_request(request.headers)
        if not data:
            return None, None
        return self.get_user(data["user_id"]), None

    def get_user(self, user_id):
        try:
            user = CustomUser.objects.get(id=user_id)
            return user
        except Exception:
            return None

    def validate_request(self, headers):
        authorization = headers.get("Authorization", None)
        if not authorization:
            return None
        token = headers['Authorization'][7:]
        decoded_data = Authentication.verify_token(token)
        if not decoded_data:
            return None

        return decoded_data

    """This allows us not to initialize"""
    @staticmethod
    def verify_token(token):
        # decode token 
        try:
            decoded_data = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
        except Exception:
            return None

        # Checking if the data is expired
        exp = decoded_data["exp"]

        if datetime.now().timestamp() > exp:
            return None
    
        return decoded_data

