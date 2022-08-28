from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairViewSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairViewSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        "api/getRoutes",
        "api/token",
        "api/token/refresh",
    ]
    return Response(routes)


