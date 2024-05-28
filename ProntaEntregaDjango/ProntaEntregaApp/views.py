# Django imports
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, JsonResponse

# Django REST Framework imports
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.views import APIView
from rest_framework import generics, status, exceptions, permissions
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token

# Application-specific imports
from ProntaEntregaApp.serializers.userSerializers import *
from ProntaEntregaApp.models import Usuario
from ProntaEntregaApp.validations import *



def index(request):
    return render(request, 'index.html')

def ver_usuarios(request):
    # Obtener todos los usuarios de la base de datos
    usuarios = Usuario.objects.all()

    # Serializar los usuarios a JSON
    usuarios_json = []
    for usuario in usuarios:
        usuario_json = {
            'id': usuario.id_usuario,
            'nombre': usuario.nombre,
            'apellido': usuario.apellido,
            'nombre_usuario': usuario.nombreusuario,
            'documento': usuario.documento,
            'telefono': usuario.telefono,
            'email': usuario.email,
            'genero': usuario.genero,
            'fecha_union': usuario.fechaUnion,
            'last_login': usuario.last_login,
            'is_superuser': usuario.is_superuser,
            'id_direccion': usuario.id_direccion_id,
            'id_tipo_usuario': usuario.id_tipousuario_id,
            'id_tipo_documento': usuario.id_tipodocumento_id
        }
        usuarios_json.append(usuario_json)

    # Devolver la respuesta como JSON
    return JsonResponse(usuarios_json, safe=False)

class UserRegister(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UsuarioRegistroSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            if 'email' not in request.data or 'password' not in request.data:
                return Response({'error': 'El email y la contraseña son necesarias.'}, status=status.HTTP_400_BAD_REQUEST)

            user = Usuario.objects.get(email=request.data['email'])
            if not user.check_password(request.data['password']):
                return Response({'error': 'La contraseña es incorrecta.'}, status=status.HTTP_401_UNAUTHORIZED)

            token, created = Token.objects.get_or_create(user=user)
            serializer = UsuarioLoginSerializer(user)
            return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_200_OK)
        except Usuario.DoesNotExist:
            return Response({'error': 'El usuario no existe.'}, status=status.HTTP_404_NOT_FOUND)

class UserPage(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response("Exito!! {}".format(request.user.email), status=status.HTTP_200_OK)

class TestToken(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response("Exito!! {}".format(request.user.email), status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CambiarContraseña(request):
    serializer = ChangePasswordSerializer(data=request.data)
    if serializer.is_valid():
        user = request.user
        current_password = serializer.validated_data.get('current_password')
        new_password = serializer.validated_data.get('new_password')
        confirm_new_password = serializer.validated_data.get('confirm_new_password')

        if not user.check_password(current_password):
            return Response({'error': 'La contraseña actual no es correcta.'}, status=status.HTTP_400_BAD_REQUEST)

        if new_password != confirm_new_password:
            return Response({'error': 'La nueva contraseña y la confirmación no coinciden.'}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()
        return Response({'success': 'Contraseña cambiada correctamente.'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)