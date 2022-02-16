from rest_framework.decorators import api_view
from .serializers import ResgistrationSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from user_app import models
from rest_framework import status

@api_view(['POST',])
def logOut_view(request):
    if request.method == "POST":
        request.user.auth_token.delete()
        return Response({'Success': 'You are logged out and your token has been deleted'},status=status.HTTP_200_OK)

@api_view(['POST',])
def registration_view(request):
    if request.method == "POST":
        serializer = ResgistrationSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data['response'] = "Registration successful!!!"
            data['username'] = account.username
            data['email'] = account.email

            token = Token.objects.get(user=account).key
            data['token'] = token 
        else:
            data = serializer.errors
        return Response(data)
