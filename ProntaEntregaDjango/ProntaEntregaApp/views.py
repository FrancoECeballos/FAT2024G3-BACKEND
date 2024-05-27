# Django imports
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest

# Django REST Framework imports
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.views import APIView
from rest_framework import generics, status, exceptions, permissions
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authtoken.models import Token

# Application-specific imports
from ProntaEntregaApp.serializers.userSerializers import UsuarioRegistroSerializer, UsuarioLoginSerializer
from ProntaEntregaApp.models import Usuario
from ProntaEntregaApp.validations import *

@api_view(['POST'])
@permission_classes([AllowAny])
def UserRegister(request):
    serializer = UsuarioRegistroSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def UserLogin(request):
    try:
        if 'nombreusuario' not in request.data or 'password' not in request.data:
            return Response({'error': 'Invalid request data'}, status=status.HTTP_400_BAD_REQUEST)

        user = Usuario.objects.get(nombreusuario=request.data['nombreusuario'])
        if not user.check_password(request.data['password']):
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        token, created = Token.objects.get_or_create(user=user)
        serializer = UsuarioLoginSerializer(user)
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_200_OK)
    except Usuario.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("Exito!!", status=status.HTTP_200_OK)
