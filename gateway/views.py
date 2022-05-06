from django.shortcuts import render
from django_api_project.settings import SECRET_KEY
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from .models import Jwt
from user.models import CustomUser
import random
import string
from rest_framework.views import APIView
from .serializers import LoginSerializer, RegisterSerializer, RefreshSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from .authentication import Authentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
def get_random(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def get_access_token(payload):
    return jwt.encode(
        {"exp": datetime.now() + timedelta(minutes=5), **payload},
        settings.SECRET_KEY,
        algorithm="HS256"
    )

def get_refresh_token():
    return jwt.encode(
        {"exp": datetime.now() + timedelta(days=365), "data": get_random(10)},
        settings.SECRET_KEY,
        algorithm='HS256'
    )



# Now implementing the LoginView for the APIView
class LoginView(APIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )

        if not user :
            return Response({"error": "Invalid email or password" }, status=400)

        # Here we delete the user ID first before generating a new token that is going to help in the login
        # This will also help us to be able to create a new user and generate a token for that user
        Jwt.objects.filter(user_id=user.id).delete()

        access = get_access_token({"user_id": user.id})
        refresh = get_refresh_token()

        Jwt.objects.create(
            # We are decoding the token here so that a wrong access token will not be generated and hence when we need to resnd the response we will not send the decoded info.
            user_id=user.id, access=access, refresh=refresh
        )
        return Response({
            "access": access,
            "refresh": refresh
        })


class RegisterView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        CustomUser.objects._create_user(**serializer.validated_data)

        return Response({
            "success": 'User created successfully'
        })



    


class RefreshView(APIView):
    serializer_class = RefreshSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            active_jwt = Jwt.objects.get(refresh=serializer.validated_data['refresh'])
        except Jwt.DoesNotExist:
            return Response({"error": "refresh token not found"}, status="400")

        if not Authentication.verify_token(serializer.validated_data["refresh"]):
            return Response({
                "error": "Token is invalid or has expired"
            })

        access = get_access_token({"user_id": active_jwt.id})
        refresh = get_refresh_token()

        active_jwt.access = access
        active_jwt.refresh = refresh

        active_jwt.save()

        return Response({
            "access": access,
            "refresh": refresh
        })




class TestException(APIView):
    # authentication_classes = [Authentication] To set a global authentication you go and add the rest framework classes
    #permission_classes = [IsAuthenticated]

    def get(self, request):
        # print(request.user)
        # a = 2 % 0

        # we ca also handle our exceptions by ourselves
        try:
            a = 2 / 0
        except Exception as e:
            raise Exception("You cannot divide by zero")
        return Response({"data": "This is a secure info"})