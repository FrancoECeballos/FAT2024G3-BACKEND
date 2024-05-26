# Django imports
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest
from django.contrib.auth.models import *

# Django REST Framework imports
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework import generics, status, exceptions, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

# Application-specific imports
from ProntaEntregaApp.serializers.userSerializers import *
from ProntaEntregaApp.models import *
from ProntaEntregaApp.validations import *





class UsuarioRegistroAPIView(APIView):
    def post(self, request):
        serializer = UsuarioRegistroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsuarioLoginAPIView(APIView):
    def post(self, request):
        serializer = UsuarioLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(request, email=serializer.validated_data['email'], password=serializer.validated_data['contrasena'])
            if user is not None:
                login(request, user)
                return Response("Login exitoso", status=status.HTTP_200_OK)
            else:
                return Response("Credenciales inválidas", status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
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

"""