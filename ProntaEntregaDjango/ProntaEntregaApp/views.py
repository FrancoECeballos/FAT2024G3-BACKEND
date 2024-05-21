from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework import generics, status, exceptions, permissions
from rest_framework.response import Response
from ProntaEntregaApp.serializers import *
from django.http import HttpRequest
from ProntaEntregaApp.models import *
from ProntaEntregaApp.validations import *

# Create your views here.

from django.shortcuts import render

class registerView(generics.GenericAPIView):
    permissions_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = UsuarioRegistroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class userView(generics.GenericAPIView):
    permissions_classes = [permissions.AllowAny]
    authentication_classes = (SessionAuthentication,)
    def post(self, request):
        data = request.data
        assert validate_email(data)

class loginView(generics.GenericAPIView):
    def get(self, request: HttpRequest, *args, **kwargs):
        return Response ({"message": "Hello, world!"})
    
class logoutView(generics.GenericAPIView):
        def get(self, request: HttpRequest, *args, **kwargs):
            return Response ({"message": "Hello, world!"})


