from django.db import models
from user.models import CustomUser

'''This models is going to hold information about the tokens we have issued out. Its 
going to have info about the tokens we have generated and to what user we have given it to
Access Token: is the token the user needs to provide to have access to a server

Refresh token is token needed by the server to release another access token'''

# Create your models here.
class Jwt(models.Model):
    '''In this model we are trying to create a token which can reallow the user to cha'''
    user = models.OneToOneField(CustomUser, related_name='login_user', on_delete=models.CASCADE)
    access = models.TextField()
    refresh = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email