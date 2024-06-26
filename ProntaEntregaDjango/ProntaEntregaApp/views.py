# Django imports
from .models import *
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
from ProntaEntregaApp.serializers.stockSerializers import *
from ProntaEntregaApp.serializers.generalSerializers import *
from ProntaEntregaApp.serializers.offerSerializers import *
from ProntaEntregaApp.serializers.requestSerializers import *
from ProntaEntregaApp.models import CustomUsuario
from django.http import JsonResponse
from django.db.models import Count
from django.views.decorators.http import require_http_methods
import json
from django.views.decorators.csrf import csrf_exempt
from ProntaEntregaApp.emails import email_sending
from django.db.models import Count, Q 

def index(request):
    return render(request, 'index.html')

class GetDirecciones(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        direcciones = Direccion.objects.all()
        serializer = DireccionSerializer(direcciones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class GetDireccion(APIView):
    permission_classes = [AllowAny]
    def get(self, request, pk):
        try:
            direcciones = Direccion.objects.filter(id_direccion=pk)
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


class GetOrganizaciones(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        organizaciones = Organizacion.objects.all()
        serializer = OrganizacionSerializer(organizaciones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CrearOrganizaciones(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = OrganizacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditarOrganizaciones(APIView):
    def put(self, request, pk):
        try:
            organizacion = Organizacion.objects.get(pk=pk)
        except Organizacion.DoesNotExist:
            return Response({'error': 'No se encontró una organización con el ID proporcionado.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrganizacionSerializer(organizacion, data=request.data, partial=True)
        if serializer.is_valid():
            if 'nombre' in request.data and request.data['nombre'] == organizacion.nombre:
                serializer.fields['nombre'].unique = False

            serializer.save()
            return Response({'success': 'Los atributos de la organización han sido modificados exitosamente.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetTipoDocumento(APIView):
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

class CrearTipoDocumento(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = TipodocumentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EditarTipoDocumento(APIView):
    def put(self, request, pk):
        try:
            tipo_documento = Tipodocumento.objects.get(pk=pk)
        except Tipodocumento.DoesNotExist:
            return Response({'error': 'No se encontró un tipo de documento con el ID proporcionado.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TipodocumentoSerializer(tipo_documento, data=request.data, partial=True)
        if serializer.is_valid():
            if 'nombre' in request.data and request.data['nombre'] == tipo_documento.nombre:
                serializer.fields['nombre'].unique = False

            serializer.save()
            return Response({'success': 'Los atributos del tipo de documento han sido modificados exitosamente.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetTipoUsuario(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        tipo_usuarios = Tipousuario.objects.all()

        tipo_usuarios_json = []
        for tipo_usuario in tipo_usuarios:
            tipo_usuario_json = {
                'id': tipo_usuario.id_tipousuario,
                'nombre': tipo_usuario.nombre
            }
            tipo_usuarios_json.append(tipo_usuario_json)
        return JsonResponse(tipo_usuarios_json, safe=False)

class CrearTipoUsuario(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = TipousuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditarTipoUsuario(APIView):
    def put(self, request, pk):
        try:
            tipo_usuario = Tipousuario.objects.get(pk=pk)
        except Tipousuario.DoesNotExist:
            return Response({'error': 'No se encontró un tipo de usuario con el ID proporcionado.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TipousuarioSerializer(tipo_usuario, data=request.data, partial=True)
        if serializer.is_valid():
            if 'nombre' in request.data and request.data['nombre'] == tipo_usuario.nombre:
                serializer.fields['nombre'].unique = False

            serializer.save()
            return Response({'success': 'Los atributos del tipo de usuario han sido modificados exitosamente.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

class UserByToken(APIView):
    permission_classes = [AllowAny]

    def get(self, request, token):
        try:
            usuario = CustomUsuario.objects.get(auth_token = token)
            serializer = UsuarioSerializer(usuario)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CustomUsuario.DoesNotExist:
            return Response({'error': 'El usuario no existe.'}, status=status.HTTP_404_NOT_FOUND)

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


class CambiarContrasenia_open(APIView): ##no abrir sin consultar que es esto
    permission_classes = [AllowAny]

    def get(self,request,pk):
        CodigosDeVerificacion.objects.filter(codigo__startswith=pk).delete()
        usuario = CustomUsuario.objects.get(pk = pk)
        codigo= email_sending.get_codigoVerificacion(usuario.pk)

        serializer = CodigosDeVerificacionSerializer(data={'codigo':codigo})
        if serializer.is_valid():
            serializer.save()

        email_sending.cambiar_contra(usuario.email,usuario.nombre,codigo)

        return Response({'a introducir':'codigo_necesitado,new_password,new_password_repeat'})
    
    def put(self, request,pk):
        usuario = CustomUsuario.objects.get(pk = pk)

        if 'codigo_necesitado' not in request.data or 'new_password' not in request.data or 'new_password_repeat' not in request.data:
            return Response({'error': 'Por favor, proporcione el codigo mandado a su mail, la nueva contraseña y la repetición de la nueva contraseña.'}, status=status.HTTP_400_BAD_REQUEST)

        codigo_necesitado = request.data['codigo_necesitado']
        new_password = request.data['new_password']
        new_password_repeat = request.data['new_password_repeat']

        cod_obj = CodigosDeVerificacion.objects.filter(codigo__startswith=pk).first()
        print(cod_obj.codigo)
        if codigo_necesitado != cod_obj.codigo:
            return Response({'error': 'El codigo es incorrecto.'}, status=status.HTTP_400_BAD_REQUEST)

        if new_password != new_password_repeat:
            return Response({'error': 'Las nuevas contraseñas no coinciden.'}, status=status.HTTP_400_BAD_REQUEST)

        usuario.set_password(new_password)
        usuario.save()
        return Response({'success': 'La contraseña ha sido cambiada con éxito.'}, status=status.HTTP_200_OK)

class GetCasa(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        casas = Casa.objects.all()
        serializer = CasaSerializer(casas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
  
class CrearCasa(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = CasaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
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

class GetUnidadMedida(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        unidades_medida = Unidadmedida.objects.all()

        unidades_medida_json = []
        for unidad_medida in unidades_medida:
            unidad_medida_json = {
                'id': unidad_medida.id_unidadmedida,
                'nombre': unidad_medida.nombre
            }
            unidades_medida_json.append(unidad_medida_json)
        return JsonResponse(unidades_medida_json, safe=False)

class CrearUnidadMedida(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UnidadmedidaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditarUnidadMedida(APIView):
    def put(self, request, pk):
        try:
            unidad_medida = Unidadmedida.objects.get(pk=pk)
        except Unidadmedida.DoesNotExist:
            return Response({'error': 'No se encontró una unidad de medida con el ID proporcionado.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UnidadmedidaSerializer(unidad_medida, data=request.data, partial=True)
        if serializer.is_valid():
            if 'nombre' in request.data and request.data['nombre'] == unidad_medida.nombre:
                serializer.fields['nombre'].unique = False

            serializer.save()
            return Response({'success': 'Los atributos de la unidad de medida han sido modificados exitosamente.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetStock(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        stock = Stock.objects.all()
        serializer = StockSerializer(stock, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CrearStock(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditarStock(APIView):
    def put(self, request, pk):
        try:
            stock = Stock.objects.get(pk=pk)
        except Stock.DoesNotExist:
            return Response({'error': 'No se encontró un stock con el ID proporcionado.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StockSerializer(stock, data=request.data,partial=True)

        if serializer.is_valid():

            serializer.save()
            return Response({'success': 'Los atributos del stock han sido modificados exitosamente.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class GetCategoriaProducto(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        categorias = Categoriaproducto.objects.all()
        serializer = CategoriaprodutoSerializer(categorias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CrearCategoriaProducto(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = CategoriaprodutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EditarCategoriaProducto(APIView):
    def put(self, request, pk):
        try:
            categoria = Categoriaproducto.objects.get(pk=pk)
        except Categoriaproducto.DoesNotExist:
            return Response({'error': 'No se encontró una categoría con el ID proporcionado.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CategoriaprodutoSerializer(categoria, data=request.data,partial=True)

        if serializer.is_valid():

            serializer.save()
            return Response({'success': 'Los atributos de la categoría han sido modificados exitosamente.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetProductos(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CrearProductos(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditarProducto(APIView):
    def put(self, request, pk):
        try:
            producto = Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            return Response({'error': 'No se encontró un producto con el ID proporcionado.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductoSerializer(producto, data=request.data,partial=True)

        if serializer.is_valid():

            serializer.save()
            return Response({'success': 'Los atributos del producto han sido modificados exitosamente.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetPedido(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        pedidos = Pedido.objects.all()
        serializer = PedidoSerializer(pedidos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CrearPedido(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = PedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditarPedido(APIView):
    def put(self, request, pk):
        try:
            pedido = Pedido.objects.get(pk=pk)
        except Pedido.DoesNotExist:
            return Response({'error': 'No se encontró un pedido con el ID proporcionado.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PedidoSerializer(pedido, data=request.data,partial=True)

        if serializer.is_valid():

            serializer.save()
            return Response({'success': 'Los atributos del pedido han sido modificados exitosamente.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class GetEstadoPedido(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        estados = Estadopedido.objects.all()
        serializer = EstadopedidoSerializer(estados, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CrearEstadoPedido(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = EstadopedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditarEstadoPedido(APIView):
    def put(self, request, pk):
        try:
            estado = Estadopedido.objects.get(pk=pk)
        except Estadopedido.DoesNotExist:
            return Response({'error': 'No se encontró un estado de pedido con el ID proporcionado.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EstadopedidoSerializer(estado, data=request.data,partial=True)

        if serializer.is_valid():

            serializer.save()
            return Response({'success': 'Los atributos del estado de pedido han sido modificados exitosamente.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetDetallePedido(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        detalles = Detallepedido.objects.all()
        serializer = DetallepedidoSerializer(detalles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CrearDetallePedido(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = DetallepedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditarDetallePedido(APIView):
    def put(self, request, pk):
        try:
            detalle = Detallepedido.objects.get(pk=pk)
        except Detallepedido.DoesNotExist:
            return Response({'error': 'No se encontró un detalle de pedido con el ID proporcionado.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DetallepedidoSerializer(detalle, data=request.data,partial=True)

        if serializer.is_valid():

            serializer.save()
            return Response({'success': 'Los atributos del detalle de pedido han sido modificados exitosamente.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class GetOferta(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        ofertas = Oferta.objects.all()
        serializer = OfertaSerializer(ofertas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CrearOferta(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = OfertaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditarOferta(APIView):
    def put(self, request, pk):
        try:
            oferta = Oferta.objects.get(pk=pk)
        except Oferta.DoesNotExist:
            return Response({'error': 'No se encontró una oferta con el ID proporcionado.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = OfertaSerializer(oferta, data=request.data,partial=True)

        if serializer.is_valid():

            serializer.save()
            return Response({'success': 'Los atributos de la oferta han sido modificados exitosamente.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetEstadoOferta(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        estados = Estadooferta.objects.all()
        serializer = EstadoofertaSerializer(estados, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CrearEstadoOferta(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = EstadoofertaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditarEstadoOferta(APIView):
    def put(self, request, pk):
        try:
            estado = Estadooferta.objects.get(pk=pk)
        except Estadooferta.DoesNotExist:
            return Response({'error': 'No se encontró un estado de oferta con el ID proporcionado.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EstadoofertaSerializer(estado, data=request.data,partial=True)

        if serializer.is_valid():

            serializer.save()
            return Response({'success': 'Los atributos del estado de oferta han sido modificados exitosamente.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetDetalleOferta(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        detalles = Detalleoferta.objects.all()
        serializer = DetalleofertaSerializer(detalles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CrearDetalleOferta(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = DetalleofertaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EditarDetalleOferta(APIView):
    def put(self, request, pk):
        try:
            detalle = Detalleoferta.objects.get(pk=pk)
        except Detalleoferta.DoesNotExist:
            return Response({'error': 'No se encontró un detalle de oferta con el ID proporcionado.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DetalleofertaSerializer(detalle, data=request.data,partial=True)

        if serializer.is_valid():

            serializer.save()
            return Response({'success': 'Los atributos del detalle de oferta han sido modificados exitosamente.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetTransporte(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        transportes = Transporte.objects.all()
        serializer = TransporteSerializer(transportes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CrearTransporte(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = TransporteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EditarTransporte(APIView):
    def put(self, request, pk):
        try:
            transporte = Transporte.objects.get(pk=pk)
        except Transporte.DoesNotExist:
            return Response({'error': 'No se encontró un transporte con el ID proporcionado.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TransporteSerializer(transporte, data=request.data,partial=True)

        if serializer.is_valid():

            serializer.save()
            return Response({'success': 'Los atributos del transporte han sido modificados exitosamente.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




#---------------------------------------------------------------------------------------------------------------------------
class CambiarStock(APIView):
    def put(self, request, pk):
        try:
            stock = Stock.objects.get(pk=pk)
        except Stock.DoesNotExist:
            return Response({'error': 'No se encontro un stock con el ID proporcionado.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductoSerializer(stock, data=request.data,partial=True)

        if serializer.is_valid():

            serializer.save()
            return Response({'success': 'Los atributos del stock han sido modificados exitosamente.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CambiarProducto (APIView):

    def put(self, request, pk):
        try:
            producto = Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            return Response({'error': 'No se encontro un producto con el ID proporcionado.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductoSerializer(producto, data=request.data,partial=True)

        if serializer.is_valid():

            serializer.save()
            return Response({'success': 'Los atributos del producto han sido modificados exitosamente.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CambiarDetalleStock (APIView):

    def put(self, request, pk):
        try:
            stock = Detallestockproducto.objects.get(pk=pk)
        except Detallestockproducto.DoesNotExist:
            return Response({'error': 'No se encontro un stock con el ID proporcionado.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DetallestockproductoSerializer(stock, data=request.data,partial=True)

        if serializer.is_valid():

            serializer.save()
            return Response({'success': 'Los atributos del stock han sido modificados exitosamente.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

class PostStock(APIView):
    def post(self,request):
        serializer = Stock(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostProducto(APIView):
    def post(self,request):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetallestockproducto(APIView):
    def post(self,request):
        serializer = DetallestockproductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DeleteProducto(APIView):
    def delete(self, request, pk):
        try:
            producto = get_object_or_404(Producto, id_producto=pk)
            producto.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Producto.DoesNotExist:
            return Response({'error': 'El producto no existe.'}, status=status.HTTP_404_NOT_FOUND)

class DeleteDetallestockproducto(APIView):
    def delete(self, request, pk):
        try:
            detallestockproducto = get_object_or_404(Detallestockproducto, id_detallestockproducto=pk)
            detallestockproducto.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Detallestockproducto.DoesNotExist:
            return Response({'error': 'El Detallestockproducto no existe.'}, status=status.HTTP_404_NOT_FOUND)

class DeleteStock(APIView):
    def delete(self, request, pk):
        try:
            stock = get_object_or_404(Stock, id_stock=pk)
            stock.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Stock.DoesNotExist:
            return Response({'error': 'El Stock no existe.'}, status=status.HTTP_404_NOT_FOUND)


class VerUsuarios(APIView):
    permission_classes = [AllowAny]
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
                'is_verified': usuario.is_verified,
                'id_direccion': usuario.id_direccion_id,
                'id_tipo_usuario': usuario.id_tipousuario_id,
                'id_tipo_documento': usuario.id_tipodocumento_id
            }
            usuarios_json.append(usuario_json)
        return JsonResponse(usuarios_json, safe=False)

class UserDelete(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, email):
        try:
            usuario = get_object_or_404(CustomUsuario, email=email)
            usuario.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CustomUsuario.DoesNotExist:
            return Response({'error': 'El usuario no existe.'}, status=status.HTTP_404_NOT_FOUND)
        


class UserUpdate(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, token):
        try:
            usuario = CustomUsuario.objects.get(auth_token = token)
        except CustomUsuario.DoesNotExist:
            return Response({'error': 'El usuario no existe.'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        
        serializer = UsuarioUpdateSerializer(usuario, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserUpdateEmail(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, email):
        try:
            usuario = CustomUsuario.objects.get(email = email)
        except CustomUsuario.DoesNotExist:
            return Response({'error': 'El usuario no existe.'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        
        serializer = UsuarioUpdateSerializer(usuario, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Categoria(APIView):
    def get(self, request):
        categorias = Categoriaproducto.objects.all()
        serializer = CategoriaprodutoSerializer(categorias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CategoriaDelete(APIView):
    def delete(self, request, pk):
        try:
            categoria = Categoriaproducto.objects.get(pk=pk)
            categoria.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Categoriaproducto.DoesNotExist:
            return Response({'error': 'La categoría no existe.'}, status=status.HTTP_404_NOT_FOUND)
        
class CategoriaPost(APIView):
    def post(self,request):
        serializer = CategoriaprodutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GetCasasAsignadasByEmail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, email):
        try:
            usuario = CustomUsuario.objects.get(email = email)
            detalle_casas = Detallecasausuario.objects.filter(id_usuario=usuario.id_usuario)
            serializer = DetallecasausuarioSerializer(detalle_casas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Detallecasausuario.DoesNotExist:
            return Response({'error': 'El usuario no pertenece a ninguna casa.'}, status=status.HTTP_404_NOT_FOUND)
        
class GetCasasAsignadasByToken(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, token):
        try:
            usuario = CustomUsuario.objects.get(auth_token = token)
            detalle_casas = Detallecasausuario.objects.filter(id_usuario=usuario.id_usuario)
            serializer = DetallecasausuarioSerializer(detalle_casas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Detallecasausuario.DoesNotExist:
            return Response({'error': 'El usuario no pertenece a ninguna casa.'}, status=status.HTTP_404_NOT_FOUND)
        
class DeleteDetalleCasaUsuario (APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            detalle = Detallecasausuario.objects.get(pk=pk)
            detalle.delete()
            return Response({'La relacion usuario-casa se elimino correctamente'},status=status.HTTP_204_NO_CONTENT)
        except Detallecasausuario.DoesNotExist:
            return Response({'error': 'El detalle no existe.'}, status=status.HTTP_404_NOT_FOUND)

class PostDetalleCasaUsuario(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        casa = get_object_or_404(Casa, id_casa=request.data.get('id_casa'))
        data = request.data.copy()
        data['id_casa'] = casa
        serializer = DetallecasausuarioSerializer(data=request.data, id_casa=casa)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoriasProductosView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id_casa):
        categorias = Categoriaproducto.objects.annotate(
            cantidad_productos=Count('producto__detallestockproducto__id_stock', filter=Q(producto__detallestockproducto__id_stock__id_casa=id_casa))
        ).values('nombre', 'cantidad_productos')

        return Response(categorias)

class ProductosPorCategoriaYCasaView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id_casa, id_categoriaproducto):
        try:
            # Verificar si existe la casa
            casa = get_object_or_404(Stock, id_casa=id_casa)

            # Verificar si existe la categoría de producto
            categoria = get_object_or_404(Categoriaproducto, id_categoriaproducto=id_categoriaproducto)

            # Obtener los detalles de stock para esa casa y categoría
            detalles_stock = Detallestockproducto.objects.filter(
                id_stock__id_casa=id_casa,
                id_producto__id_categoriaproducto=id_categoriaproducto
            )

            # Obtener los productos correspondientes a los detalles de stock
            productos_ids = detalles_stock.values_list('id_producto', flat=True)
            productos = Producto.objects.filter(id_producto__in=productos_ids)

            # Serializar los datos
            serializer = ProductoSerializer(productos, many=True)

            return Response(serializer.data)
        
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )