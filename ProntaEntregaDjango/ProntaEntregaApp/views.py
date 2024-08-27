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
import datetime
from django.utils import timezone
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML
from .models import Pedido
from datetime import datetime, timedelta, date

def index(request):
    return render(request, 'index.html')

class Verificar(APIView):
    def get(self,request,pk):
        user = get_object_or_404(CustomUsuario, pk=pk)
        user.is_verified = True
        user.save()
        serializer = UsuarioUpdateSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GetNotificacionesDeUser(APIView):
    permission_classes = [AllowAny]
    def get(self,request,pk):
        notif = Notificacion.objects.filter(id_usuario = pk)
        serializer = NotificacionSerializer(notif,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
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
        request.data.update({'fecha_creacion':date.today()})
        serializer = UsuarioRegistroSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            link = 'http://127.0.0.1:8000/user/Verificar/' + str(user.id_usuario)
            ## email_sending.verificar_register(user.email,user.nombre,link)
            # no borrar la linea de arriba, esta asi solo para mandar mails mas adelante
            user.set_password(request.data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            if 'user' not in request.data or 'password' not in request.data:
                return Response({'error': 'El nombre de usuario/email y la contraseña son necesarias.'}, status=status.HTTP_400_BAD_REQUEST)

            user = CustomUsuario.objects.get(Q(email=request.data['user']) | Q(nombreusuario=request.data['user']))
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


class UserByID(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        usuario = get_object_or_404(CustomUsuario, pk=pk)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserByToken(APIView):
    permission_classes = [AllowAny]

    def get(self, request, token):
        try:
            usuario = CustomUsuario.objects.get(auth_token = token)
            serializer = UsuarioSerializer(usuario)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CustomUsuario.DoesNotExist:
            return Response({'error': 'El usuario no existe.'}, status=status.HTTP_404_NOT_FOUND)
        
class AllUsersByObra(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        usr = CustomUsuario.objects.all()
        serializer = UsuarioSerializer(usr, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AllUsersByObra_null(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        detalles = Detalleobrausuario.objects.all().values_list('id_usuario', flat=True)
        usr = CustomUsuario.objects.exclude(id_usuario__in = detalles).exclude(is_superuser = True)
        serializer = UsuarioSerializer(usr, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
class ObraByUser(APIView):
    permission_classes = [AllowAny]

    def get(self, request, token):
        detalles = Detalleobrausuario.objects.filter(id_usuario__auth_token=token).values_list('id_obra', flat=True)
        obras = Obra.objects.filter(id_obra__in=detalles)
        serializer = ObraSerializer(obras, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ObraSinUsuario(APIView):
    permission_classes = [AllowAny]

    def get(self, request, token):
        detalles = Detalleobrausuario.objects.filter(id_usuario__auth_token=token).values_list('id_obra', flat=True)
        obras = Obra.objects.exclude(id_obra__in=detalles)
        serializer = ObraSerializer(obras, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

        
class UserByObra(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id_obra):
        detalles = Detalleobrausuario.objects.filter(id_obra=id_obra).values_list('id_usuario', flat=True)
        usuarios = CustomUsuario.objects.filter(id_usuario__in=detalles)
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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

class GetObra(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        obras = Obra.objects.all()
        serializer = ObraSerializer(obras, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class GetObraByID(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        obras = Obra.objects.filter(id_obra=pk)
        serializer = ObraSerializer(obras, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
  
class CrearObra(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = ObraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
class EditarObra(APIView):
    def put(self, request, pk):
        # Obtener la obra a modificar
        try:
            obra = Obra.objects.get(pk=pk)
        except Obra.DoesNotExist:
            return Response({'error': 'No se encontró una obra con el ID proporcionado.'}, status=status.HTTP_404_NOT_FOUND)

        # Crear un serializador con los datos recibidos y la instancia de la obra
        serializer = EditarObraSerializer(obra, data=request.data, partial=True)

        # Verificar si los datos son válidos y guardar los cambios si corresponde
        if serializer.is_valid():
            # Excluir la validación única para el nombre si el nombre no se ha modificado
            if 'nombre' in request.data and request.data['nombre'] == obra.nombre:
                serializer.fields['nombre'].unique = False

            serializer.save()
            return Response({'success': 'Los atributos de la obra han sido modificados exitosamente.'}, status=status.HTTP_200_OK)
        else:
            # Si hay errores en los datos proporcionados, devolver los errores
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetStock(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        stock = Stock.objects.all()
        serializer = StockSerializer(stock, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GetStockByID(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id_obra):
        stock = Stock.objects.filter(id_obra=id_obra)
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

class GetCategoria(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class GetCategoriaByID(APIView):
    permission_classes = [AllowAny]
    def get(self, request, id_categoria):
        categorias = Categoria.objects.filter(id_categoria=id_categoria)
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CrearCategoria(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EditarCategoria(APIView):
    def put(self, request, pk):
        try:
            categoria = Categoria.objects.get(pk=pk)
        except Categoria.DoesNotExist:
            return Response({'error': 'No se encontró una categoría con el ID proporcionado.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CategoriaSerializer(categoria, data=request.data,partial=True)

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
    
class GetProductoById(APIView):
    permission_classes = [AllowAny]
    def get(self, request, pk):
        try:
            productos = Producto.objects.filter(id_producto=pk)
        except Producto.DoesNotExist:
            return Response({'error': 'No se encontró un producto con el ID proporcionado.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CrearProductos(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = CreateProductoSerializer(data=request.data)
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
        all = []

        for p in pedidos:
            serializer = PedidoSerializer(p)

            total = 0
            aportes = AportePedido.objects.filter(id_pedido = p.id_pedido)

            for a in aportes:
                total = total + a.cantidad

            s = serializer.data
            s.update({"progreso":total})
            all.append(s)
            
            print(total)
        return Response(all, status=status.HTTP_200_OK)

class CrearPedido(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = CreatePedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostNotificacion(APIView):
    def post(self,request):
        serializer = NotificacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetUsuariosPorPedido(APIView):
    def get(self,request,id_pedido):
        

        
        detalle = Detalleobrapedido.objects.filter(pk = id_pedido)
        print(detalle.__len__())
        if detalle.__len__() == 0:
            return Response({'Error':'la tabla no existe'})

        usr_ids = []
        for o in detalle:
            for d in Detalleobrausuario.objects.filter(id_obra = o.id_obra):
                for usr in CustomUsuario.objects.filter(pk = d.id_usuario.__dict__['id_usuario']):
                    usr_ids.append(usr.pk)
        
        usuarios = CustomUsuario.objects.filter(id_usuario__in = usr_ids)
        print(usuarios)

        serializer = UsuarioSerializer(usuarios, many= True)
        return Response(serializer.data , status=status.HTTP_201_CREATED)


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

class GetDetalleobrapedido(APIView):
    def get(self, request):
        detalles = Detalleobrapedido.objects.all()
        serializer = DetalleobrapedidoSerializer(detalles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CrearDetalleobrapedido(APIView):
    def post(self, request):
        serializer = CreateDetalleobrapedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteDetalleobrapedido(APIView):
    def delete(self, request, pk):
        try:
            producto = get_object_or_404(Detalleobrapedido, id_detalleobrapedido=pk)
            producto.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Producto.DoesNotExist:
            return Response({'error': 'El producto no existe.'}, status=status.HTTP_404_NOT_FOUND)

class GetAportePedido(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        detalles = AportePedido.objects.all()
        serializer = AportePedidoSerializer(detalles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CrearAportePedido(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = CreateAportePedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditarAportePedido(APIView):
    def put(self, request, pk):
        try:
            aporte = AportePedido.objects.get(pk=pk)
        except AportePedido.DoesNotExist:
            return Response({'error': 'No se encontró un detalle de pedido con el ID proporcionado.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AportePedidoSerializer(aporte, data=request.data,partial=True)

        if serializer.is_valid():
            
            serializer.save()

            ## SECCION NOTIFICACION
            pedido= Pedido.objects.get(pk=aporte.__dict__['id_pedido_id'])

            producto = Producto.objects.get(pk=pedido.__dict__['id_producto_id'])
            
            
            serializerN = NotificacionSerializer(data={'titulo':'Se modifico su pedido','descripcion':'su pedido de '+producto.nombre+' se modifico','fecha_creacion':str(timezone.now().date()),'id_usuario':1})
            if serializerN.is_valid():
                serializerN.save()
            ##FIN SECCION NOTIFICACION


            return Response({'success': 'Los atributos del detalle de pedido han sido modificados exitosamente.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class GetOferta(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        ofertas = Oferta.objects.all()
        serializer = OfertaSerializer(ofertas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class GetOfertaById(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, pk):
        try:
            oferta = Oferta.objects.get(pk=pk)
            serializer = OfertaSerializer(oferta)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Oferta.DoesNotExist:
            return Response({'error': 'Oferta no encontrada'}, status=status.HTTP_404_NOT_FOUND)


class CrearOferta(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = CrearOfertaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetOfertaSimilar(APIView):
    def get(self,request,id_obra,id_producto):
        try:
            oferta = Oferta.objects.filter(id_obra = id_obra, id_producto = id_producto, id_estadooferta = 1)
            serializer = OfertaSerializer(oferta, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Oferta.DoesNotExist:
            return Response({'error': 'Oferta no encontrada'}, status=status.HTTP_404_NOT_FOUND)


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
        detalles = AporteOferta.objects.all()
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
            detalle = AporteOferta.objects.get(pk=pk)
        except AporteOferta.DoesNotExist:
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
    
class GetTransporteByObra(APIView):
    permission_classes = [AllowAny]
    def get(self, request, id_obra):
        try:
            detalle = Detalleobratransporte.objects.filter(id_obra = id_obra)
        except Detalleobratransporte.DoesNotExist():
            return Response({'error':'no se encuentra nada con esa id'}, status=status.HTTP_200_OK)

        transporte_ids = detalle.values_list('id_transporte', flat=True)
        
        transportes = Transporte.objects.filter(id_transporte__in=transporte_ids)
        serializer = TransporteSerializer(transportes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CrearTransporte(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = crearTransporteSerializer(data=request.data)
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
        
class EliminarTransporte(APIView):
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, id_obra, id_transporte):
        try:
            detalle = Detalleobratransporte.objects.get(id_obra=id_obra, id_transporte=id_transporte)
        except Detalleobratransporte.DoesNotExist:
            return Response({'error': 'No se encontró un detalle de obra transporte con el ID proporcionado.'}, status=status.HTTP_404_NOT_FOUND)
        
        detalle.delete()
        return Response({'success': 'El detalle de obra transporte ha sido eliminado exitosamente.'}, status=status.HTTP_200_OK)
    
class GetDetalleobratransporte(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        detalles = Detalleobratransporte.objects.all()
        serializer = DetalleobratransporteSerializer(detalles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class PostDetalleobratransporte(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = DetalleobratransporteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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
        productos_de_categoria = Producto.objects.filter(categoria_id=categoria_id)
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

class GetProductoByStock(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, id_stock,id_categoria):
        try:
            stock = Stock.objects.get(pk=id_stock)
            detalle = Detallestockproducto.objects.filter(id_stock = stock.id_stock)
            ids = []
            for y in Producto.objects.filter(id_categoria = id_categoria):
                for x in detalle:
                    if y.__dict__['id_producto'] == x.__dict__['id_producto_id']:
                        ids.append(x.__dict__['id_producto_id'])
            
            productos = Producto.objects.filter(id_producto__in = ids)

            serializer = ProductoSerializer(productos,many=True)
            for x in serializer.data:
                detalle = Detallestockproducto.objects.filter(id_stock=id_stock, id_producto=x['id_producto'])
                total = 0
                for y in detalle:
                    total = total + y.cantidad
                x.update({'total':total})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Oferta.DoesNotExist:
            return Response({'error': 'Oferta no encontrada'}, status=status.HTTP_404_NOT_FOUND)



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

    def get(self,request):
        return Response({"id_stock":1,"id_producto":1,"cantidad":1})

    def post(self,request):
        
        request.data.update({'fecha_creacion':timezone.now()})
        serializer = CrearDetallestockproductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            dd = timedelta(days=7)
            d = timezone.now() - dd
            crear_checkpoint = True
            for x in Detallestockproducto.objects.filter(id_stock = request.data['id_stock'],id_producto = request.data['id_producto'],checkpoint = True):
                if x.fecha_creacion >= d:
                    crear_checkpoint = False
            
            if crear_checkpoint == True:

                ultimo_checkpoint = Detallestockproducto.objects.filter(id_stock=request.data['id_stock'], id_producto=request.data['id_producto'],checkpoint= True)
                
                ultimo_checkpoint = ultimo_checkpoint.order_by('fecha_creacion').first()
                
                try:
                    print(ultimo_checkpoint.fecha_creacion)
                    detalle = Detallestockproducto.objects.filter(id_stock=request.data['id_stock'], id_producto=request.data['id_producto'], fecha_creacion__gt = ultimo_checkpoint.fecha_creacion)
                    total = ultimo_checkpoint.cantidad
                except AttributeError:
                    detalle = Detallestockproducto.objects.filter(id_stock=request.data['id_stock'], id_producto=request.data['id_producto'])
                    total = 0
                
                for x in detalle:
                    print(x.cantidad)
                    total = total + x.cantidad

                Detallestockproducto.objects.create(
                checkpoint=True,
                fecha_creacion=datetime.today(),
                cantidad=total,
                id_producto_id=request.data['id_producto'],
                id_stock_id=request.data['id_stock']
                )
                print('se creo checkpoint')
            else:
                print('no se necesita crear checkpoint')
            
            
             ## esto tiene que quedar al despues de todo el resto
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RestarDetallestockproducto(APIView):
    def post(self,request):
        
        try:
            request.data['cantidad']= request.data['cantidad'] * -1
        except KeyError:
            return Response({'error','se requiere una cantidad'})
        request.data.update({'fecha_creacion':datetime.today()})
        serializer = CrearDetallestockproductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
        
class DeleteProducto(APIView):
    def delete(self, request, pk):
        try:
            producto = get_object_or_404(Producto, id_producto=pk)
            producto.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Producto.DoesNotExist:
            return Response({'error': 'El producto no existe.'}, status=status.HTTP_404_NOT_FOUND)


class VerUsuarios(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        usuarios = CustomUsuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

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

class CategoriaDelete(APIView):
    def delete(self, request, pk):
        try:
            categoria = Categoria.objects.get(pk=pk)
            categoria.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Categoria.DoesNotExist:
            return Response({'error': 'La categoría no existe.'}, status=status.HTTP_404_NOT_FOUND)
        
class CategoriaPost(APIView):
    def post(self,request):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            for usr in CustomUsuario.objects.all():
                serializerN = NotificacionSerializer(data={"titulo":"Se creo una nueva categoria de producto","descripcion":'Se creo una nueva categoria "'+ request.data['nombre'],"fecha_creacion":str(timezone.now()),"id_usuario": usr.id_usuario })
                if serializerN.is_valid():
                    serializerN.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetObrasAsignadasByEmail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, email):
        try:
            usuario = CustomUsuario.objects.get(email = email)
            detalle_obras = Detalleobrausuario.objects.filter(id_usuario=usuario.id_usuario)
            serializer = DetalleobrausuarioSerializer(detalle_obras, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Detalleobrausuario.DoesNotExist:
            return Response({'error': 'El usuario no pertenece a ninguna obra.'}, status=status.HTTP_404_NOT_FOUND)
        
class GetObrasAsignadasByToken(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, token):
        try:
            usuario = CustomUsuario.objects.get(auth_token = token)
            detalle_obras = Detalleobrausuario.objects.filter(id_usuario=usuario.id_usuario)
            serializer = DetalleobrausuarioSerializer(detalle_obras, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Detalleobrausuario.DoesNotExist:
            return Response({'error': 'El usuario no pertenece a ninguna obra.'}, status=status.HTTP_404_NOT_FOUND)
        
class GetStockAsignadoByEmail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, email):
        try:
            usuario = CustomUsuario.objects.get(email = email)
            detalle_obras = Detalleobrausuario.objects.filter(id_usuario=usuario.id_usuario)
            serializer = StockSerializer(detalle_obras, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Detalleobrausuario.DoesNotExist:
            return Response({'error': 'El usuario no pertenece a ninguna obra.'}, status=status.HTTP_404_NOT_FOUND)
        
class GetStockAsignadoByToken(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, token):
        try:
            usuario = CustomUsuario.objects.get(auth_token = token)
            detalle_obras = Detalleobrausuario.objects.filter(id_usuario=usuario.id_usuario)
            serializer = StockSerializer(detalle_obras, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Detalleobrausuario.DoesNotExist:
            return Response({'error': 'El usuario no pertenece a ninguna obra.'}, status=status.HTTP_404_NOT_FOUND)
        
class DeleteDetalleObraUsuario (APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            detalle = Detalleobrausuario.objects.get(pk=pk)
            detalle.delete()
            return Response({'La relacion usuario-obra se elimino correctamente'},status=status.HTTP_204_NO_CONTENT)
        except Detalleobrausuario.DoesNotExist:
            return Response({'error': 'El detalle no existe.'}, status=status.HTTP_404_NOT_FOUND)


class PostDetalleObraUsuario(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = DetalleobrausuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductosPorCategoriaYObraView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id_stock, id_categoria):

        productos = Detallestockproducto.objects.filter(id_stock=id_stock, id_producto__id_categoria=id_categoria)
        serializer = DetallestockproductoSerializer(productos, many=True)
        return Response(serializer.data)

class UpdateDetallestockproductoView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, id_detallestockproducto):
        try:
            detalle = Detallestockproducto.objects.get(pk=id_detallestockproducto)
        except Detallestockproducto.DoesNotExist:
            return Response({'error': 'DetalleStockProducto no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        
        allowed_fields = {'cantidad', 'cantidadUnidades'}
        data = request.data

        # Verificar que solo los campos permitidos están en el cuerpo de la solicitud
        for field in data:
            if field not in allowed_fields:
                return Response({'error': f'El campo "{field}" no se puede actualizar.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = DetallestockproductoSerializer(detalle, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetallestockproductoView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        detalles = Detallestockproducto.objects.all()
        serializer = DetallestockproductoSerializer(detalles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreateDetallestockproductoView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CrearDetallestockproductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GetDetallestockproductoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id_detallestockproducto):
        try:
            detalle = Detallestockproducto.objects.get(pk=id_detallestockproducto)
            serializer = DetallestockproductoSerializer(detalle)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Detallestockproducto.DoesNotExist:
            return Response({'error': 'DetalleStockProducto no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

class GetDetallestockproducto_Total(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id_stock,id_categoria):

        todo = []

        for producto in Producto.objects.filter(id_categoria = id_categoria):
            ultimo_checkpoint = Detallestockproducto.objects.filter(id_stock=id_stock, id_producto=producto.id_producto,checkpoint= True)
            
            ultimo_checkpoint = ultimo_checkpoint.order_by('fecha_creacion').first()
        
            try:
                detalle = Detallestockproducto.objects.filter(id_stock=id_stock, id_producto=producto.id_producto, fecha_creacion__gt = ultimo_checkpoint.fecha_creacion)
                total = ultimo_checkpoint.cantidad
            except AttributeError:
                print('AttributeError, se usan todos los detalles y total es 0')
                detalle = Detallestockproducto.objects.filter(id_stock=id_stock, id_producto=producto.id_producto)
                total = 0
            
            for x in detalle:
                total = total + x.cantidad

            p = Producto.objects.get(pk = producto.id_producto)

            serializer = ProductoSerializer(p)
            d = serializer.data
            d.update({'total':total})
            todo.append(d)
        
        return Response(todo, status=status.HTTP_200_OK)

class GetCantidadTotalProductoObra(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id_stock, id_producto):
        ultimo_checkpoint = Detallestockproducto.objects.filter(id_stock=id_stock, id_producto=id_producto,checkpoint= True)
            
        ultimo_checkpoint = ultimo_checkpoint.order_by('fecha_creacion').first()
    
        try:
            detalle = Detallestockproducto.objects.filter(id_stock=id_stock, id_producto=id_producto, fecha_creacion__gt = ultimo_checkpoint.fecha_creacion)
            total = ultimo_checkpoint.cantidad
        except AttributeError:
            print('AttributeError, se usan todos los detalles y total es 0')
            detalle = Detallestockproducto.objects.filter(id_stock=id_stock, id_producto=id_producto)
            total = 0
        
        for x in detalle:
            total = total + x.cantidad

        p = Producto.objects.get(pk = id_producto)

        serializer = ProductoSerializer(p)
        d = serializer.data
        d.update({'total':total})

        return Response(d,status=status.HTTP_200_OK)
  
class DeleteDetallestockproductoView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, id_detallestockproducto):
        try:
            detalle = Detallestockproducto.objects.get(pk=id_detallestockproducto)
            detalle.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Detallestockproducto.DoesNotExist:
            return Response({'error': 'DetalleStockProducto no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

class PedidoInformePDFView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        pedidos = Pedido.objects.all()

        # Renderizar el contenido a una plantilla HTML
        html_string = render_to_string('informePedidos.html', {'pedidos': pedidos})
        
        # Generar el PDF
        pdf_file = HTML(string=html_string).write_pdf()

        current_time = datetime.now() + timedelta(hours=-3)
        formatted_time = current_time.strftime("%Y-%m-%d_%H-%M")

        # Enviar el PDF como respuesta
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="informe_pedidos_{formatted_time}.pdf"'
        return response

class StockInformePDFView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id_stock, id_producto, token):

        try:
            user = CustomUsuario.objects.get(auth_token=token)
            serializer = UsuarioSerializer(user)
            user_data = serializer.data
        except CustomUsuario.DoesNotExist:
            user_data = {'error': 'El usuario no existe.'}

        # Obtener la obra a la que pertenece el stock
        obra = Stock.objects.get(id_stock=id_stock).id_obra

        # Obtener el nombre de la obra
        nombre_obra = obra.nombre
        # Obtener el stock y el producto específico
        stocks = Stock.objects.filter(id_stock=id_stock)
        producto = Producto.objects.get(id_producto=id_producto)

        # Filtrar los detalles del stock de ese producto
        preDetalles = Detallestockproducto.objects.filter(id_producto=id_producto, id_stock__in=stocks, checkpoint=False)

        # Serializar los datos
        detalles = DetallestockproductoSerializer(preDetalles, many=True).data


        # Obtener el usuario loggeado y la fecha actual
        current_time = datetime.now() + timedelta(hours=-3)
        formatted_time = current_time.strftime("%Y-%m-%d_%H-%M")


        # Renderizar el contenido a una plantilla HTML con detalles y producto
        html_string = render_to_string('informeStock.html', {
            'detalles': detalles,
            'producto': producto,
            'fecha_generacion': formatted_time,
            'usuario': user_data,
            'obra': nombre_obra
        })
        
        # Generar el PDF
        pdf_file = HTML(string=html_string).write_pdf()

        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="informe_stock_{detalles[0]["id_producto"]["nombre"]}_{detalles[0]["id_stock"]["id_obra"]["nombre"]}_{formatted_time}.pdf"'
        return response

class GetProductosPorCategoriaExcluidos(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id_categoria):
        
        excluded_ids = request.data.get('excluded_ids', [])
        print(excluded_ids)

        if id_categoria:
            productos = Producto.objects.filter(id_categoria=id_categoria).exclude(id_producto__in=excluded_ids)
        else:
            return Response({"error": "Categoria no proporcionada"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DeletePedido(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            pedido = Pedido.objects.get(pk=pk)
            aportes = AportePedido.objects.filter(id_pedido=pedido.id_pedido)
            aportes.delete()
            pedido.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Pedido.DoesNotExist:
            return Response({'error': 'Pedido no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        

class GetDetallesProductoObra(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id_obra, id_producto):
        stocks = Stock.objects.filter(id_obra=id_obra)        # 1. Obtener el usuario que está loggeado
        user = request.user
        detalles = Detallestockproducto.objects.filter(id_producto=id_producto, id_stock__in=stocks, checkpoint=False)
        serializer = DetallestockproductoSerializer(detalles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GetPedidosByUser(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, token):
        user = CustomUsuario.objects.get(auth_token=token)

        detalles_obras_usuario = Detalleobrausuario.objects.filter(id_usuario=user)

        obras = Obra.objects.filter(id_obra__in=detalles_obras_usuario.values_list('id_obra', flat=True))
        
        stocks = Stock.objects.filter(id_obra__in=obras.values_list('id_obra', flat=True))

        detalle_obrapedidos = Detalleobrapedido.objects.filter(id_stock__in=stocks.values_list('id_stock', flat=True))

        pedidos = Pedido.objects.filter(id_pedido__in=detalle_obrapedidos.values_list('id_pedido', flat=True))

        pedidos_por_obra = []

        for obra in obras:
            obra_serialized = ObraSerializer(obra).data
            obra_pedidos = pedidos.filter(id_pedido__in=detalle_obrapedidos.filter(id_stock__in=stocks.filter(id_obra=obra).values_list('id_stock', flat=True)).values_list('id_pedido', flat=True))
            
            pedidos_serialized = []
            for pedido in obra_pedidos:
                pedido_data = PedidoSerializer(pedido).data
                detalle_pedido = detalle_obrapedidos.get(id_pedido=pedido.id_pedido)
                pedido_data['id_detalleobrapedido'] = detalle_pedido.id_detalleobrapedido
                pedidos_serialized.append(pedido_data)

            pedidos_por_obra.append({
                'obra': obra_serialized,
                'pedidos': pedidos_serialized
            })

        return Response(pedidos_por_obra, status=status.HTTP_200_OK)


class GetPedidosForAdmin(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        obras = Obra.objects.all()
        obras_con_pedidos = []

        for obra in obras:
            stocks = Stock.objects.filter(id_obra=obra.id_obra)
            detalle_obrapedidos = Detalleobrapedido.objects.filter(id_stock__in=stocks)
            pedidos = Pedido.objects.filter(id_pedido__in=detalle_obrapedidos.values_list('id_pedido', flat=True))

            obra_serialized = ObraSerializer(obra).data
            pedidos_serialized = PedidoSerializer(pedidos, many=True).data

            obras_con_pedidos.append({
                'obra': obra_serialized,
                'pedidos': pedidos_serialized
            })

        return Response(obras_con_pedidos, status=status.HTTP_200_OK)
    
class UpdateEstadoByVencimiento(APIView):
    def get(self,request):
        pedidos = Pedido.objects.all()
        ofertas = Oferta.objects.all()
        for oferta in ofertas:
            if oferta.fecha_vencimiento < date.today():
                oferta.id_estadooferta = 5
                oferta.save()
        for pedido in pedidos:
            if pedido.fecha_entrega < date.today():
                pedido.id_estado = 5
                pedido.save()
        return Response({'success': 'Los estados de los pedidos y las ofertas han sido actualizados exitosamente.'}, status=status.HTTP_200_OK)
