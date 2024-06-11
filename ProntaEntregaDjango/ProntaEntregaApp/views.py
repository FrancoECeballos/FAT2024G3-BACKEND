# Django imports
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
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
from rest_framework.permissions import AllowAny


# Application-specific imports
from ProntaEntregaApp.serializers.userSerializers import *
from ProntaEntregaApp.models import CustomUsuario
from django.http import JsonResponse



def index(request):
    return render(request, 'index.html')

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

            user = CustomUsuario.objects.get(email=request.data['email'])
            if not user.check_password(request.data['password']):
                return Response({'error': 'El usuario o la contraseña es incorrecta.'}, status=status.HTTP_401_UNAUTHORIZED)

            token, created = Token.objects.get_or_create(user=user)
            serializer = UsuarioLoginSerializer(user)
            return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_200_OK)
        except CustomUsuario.DoesNotExist:
            return Response({'error': 'El usuario no fue encontrado'}, status=status.HTTP_404_NOT_FOUND)


class DeleteUser(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            user = CustomUsuario.objects.get(pk=pk)
            user.delete()
            return Response({'success': 'El usuario ha sido eliminado con éxito.'}, status=status.HTTP_200_OK)
        except CustomUsuario.DoesNotExist:
            return Response({'error': 'Usuario no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserPage(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response("Exito!! {}".format(request.user.email), status=status.HTTP_200_OK)

class UserByEmail(APIView):
    permission_classes = [AllowAny]

    def get(self, request, email):
        try:
            usuario = CustomUsuario.objects.get(email = email)
            serializer = UsuarioSerializer(usuario)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CustomUsuario.DoesNotExist:
            return Response({'error': 'El usuario no existe.'}, status=status.HTTP_404_NOT_FOUND)

class TestToken(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response("Exito!! {}".format(request.user.email), status=status.HTTP_200_OK)


class CambiarContrasenia(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user

        if 'old_password' not in request.data or 'new_password' not in request.data or 'new_password_repeat' not in request.data:
            return Response({'error': 'Por favor, proporcione la contraseña antigua, la nueva contraseña y la repetición de la nueva contraseña.'}, status=status.HTTP_400_BAD_REQUEST)

        old_password = request.data['old_password']
        new_password = request.data['new_password']
        new_password_repeat = request.data['new_password_repeat']

        if not user.check_password(old_password):
            return Response({'error': 'La contraseña antigua es incorrecta.'}, status=status.HTTP_400_BAD_REQUEST)

        if new_password != new_password_repeat:
            return Response({'error': 'Las nuevas contraseñas no coinciden.'}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()

        return Response({'success': 'La contraseña ha sido cambiada con éxito.'}, status=status.HTTP_200_OK)
    

class VerStockYProducto(APIView):
    def get(self, request, categoria_id):
        productos_de_categoria = Producto.objects.filter(id_categoriaproducto=categoria_id)
        productos_con_stock = []

        for producto in productos_de_categoria:
            detalle_stock = Detallestockproducto.objects.filter(id_producto=producto.id_producto).first()
            cantidad_stock = detalle_stock.cantidad if detalle_stock else 0

            producto_con_stock = {
                'nombre_producto': producto.nombre,
                'descripcion': producto.descripcion,
                'stock_disponible': cantidad_stock
            }
            productos_con_stock.append(producto_con_stock)
        
        return JsonResponse(productos_con_stock, safe=False)


class VerUsuarios(APIView):
    def get(self, request):
        usuarios = CustomUsuario.objects.all()

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
        return JsonResponse(usuarios_json, safe=False)
    
class verTipoDocumento(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        tipo_documentos = Tipodocumento.objects.all()

        tipo_documentos_json = []
        for tipo_documento in tipo_documentos:
            tipo_documento_json = {
                'id': tipo_documento.id_tipodocumento,
                'nombre': tipo_documento.nombre
            }
            tipo_documentos_json.append(tipo_documento_json)
        return JsonResponse(tipo_documentos_json, safe=False)
    
class CasaPost(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = CasaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CasaGet(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        casas = Casa.objects.all()
        serializer = CasaSerializer(casas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class EditarCasa(APIView):
    def put(self, request, pk):
        # Obtener la casa a modificar
        try:
            casa = Casa.objects.get(pk=pk)
        except Casa.DoesNotExist:
            return Response({'error': 'No se encontró una casa con el ID proporcionado.'}, status=status.HTTP_404_NOT_FOUND)

        # Crear un serializador con los datos recibidos y la instancia de la casa
        serializer = EditarCasaSerializer(casa, data=request.data, partial=True)

        # Verificar si los datos son válidos y guardar los cambios si corresponde
        if serializer.is_valid():
            # Excluir la validación única para el nombre si el nombre no se ha modificado
            if 'nombre' in request.data and request.data['nombre'] == casa.nombre:
                serializer.fields['nombre'].unique = False

            serializer.save()
            return Response({'success': 'Los atributos de la casa han sido modificados exitosamente.'}, status=status.HTTP_200_OK)
        else:
            # Si hay errores en los datos proporcionados, devolver los errores
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDelete(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            usuario = get_object_or_404(CustomUsuario, id_usuario=pk)
            usuario.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CustomUsuario.DoesNotExist:
            return Response({'error': 'El usuario no existe.'}, status=status.HTTP_404_NOT_FOUND)
        
class GetDirecciones(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        direcciones = Direccion.objects.all()
        serializer = DireccionSerializer(direcciones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class GetDireccion(APIView):
    permission_classes = [AllowAny]
    def get(self, request, calle, numero, localidad):
        try:
            direcciones = Direccion.objects.filter(localidad=localidad, numero=numero, calle=calle)
        except Direccion.DoesNotExist:
            return Response({'error': 'No se encontró una dirección con los datos proporcionado.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DireccionSerializer(direcciones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

class CrearDirecciones(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = DireccionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditarDirecciones(APIView):
    def put(self, request, pk):
        try:
            direccion = Direccion.objects.get(pk=pk)
        except Direccion.DoesNotExist:
            return Response({'error': 'No se encontró una dirección con el ID proporcionado.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DireccionSerializer(direccion, data=request.data, partial=True)
        if serializer.is_valid():
            if 'nombre' in request.data and request.data['nombre'] == direccion.nombre:
                serializer.fields['nombre'].unique = False

            serializer.save()
            return Response({'success': 'Los atributos de la dirección han sido modificados exitosamente.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserUpdate(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        try:
            usuario = CustomUsuario.objects.get(pk=pk)
        except CustomUsuario.DoesNotExist:
            return Response({'error': 'El usuario no existe.'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        if 'password' in data:
            return Response({'error': 'No se puede actualizar la contraseña a través de esta operación. Utiliza el metodo cambiar_contrasenia'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UsuarioSerializer(usuario, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

