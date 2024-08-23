from rest_framework import serializers
from ProntaEntregaApp.models import *
from ProntaEntregaApp.serializers.stockSerializers import *
from ProntaEntregaApp.serializers.generalSerializers import ObraSerializer
from ProntaEntregaApp.serializers.userSerializers import UsuarioSerializer
from django.contrib.auth import authenticate

class DetallepedidoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AportePedido
        fields = '__all__'

class EstadopedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadopedido
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    id_obra = ObraSerializer()
    id_usuario = UsuarioSerializer()
    id_producto = ProductoSerializer()

    class Meta:
        model = Pedido
        fields = '__all__'

class PedidoSerializerPorObra(serializers.ModelSerializer):
    id_usuario = UsuarioSerializer()
    id_producto = ProductoSerializer()

    class Meta:
        model = Pedido
        fields = '__all__'

class CreatePedidoSerializer(serializers.ModelSerializer):
    id_obra = serializers.PrimaryKeyRelatedField(queryset=Obra.objects.all())
    id_usuario = serializers.PrimaryKeyRelatedField(queryset=CustomUsuario.objects.all())
    id_estadoPedido = serializers.PrimaryKeyRelatedField(queryset=Estadopedido.objects.all())
    id_producto = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all())
    fechainicio = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"])
    fechavencimiento = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"])

    class Meta:
        model = Pedido
        fields = '__all__'
        