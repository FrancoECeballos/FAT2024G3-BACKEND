from rest_framework import serializers
from ProntaEntregaApp.models import *
from ProntaEntregaApp.serializers.stockSerializers import *
from ProntaEntregaApp.serializers.generalSerializers import ObraSerializer
from ProntaEntregaApp.serializers.userSerializers import UsuarioSerializer
from django.contrib.auth import authenticate

class AportePedidoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AportePedido
        fields = '__all__'

class CreateAportePedidoSerializer(serializers.ModelSerializer):
    id_pedido = serializers.PrimaryKeyRelatedField(queryset=Pedido.objects.all())
    id_usuario = serializers.PrimaryKeyRelatedField(queryset=CustomUsuario.objects.all())
    cantidad = serializers.FloatField()
    fecha = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"])

    class Meta:
        model = AportePedido
        fields = ['id_usuario', 'fecha', 'cantidad', 'id_pedido']

    def create(self, validated_data):
        id_usuario = validated_data.pop('id_usuario')
        fecha = validated_data.pop('fecha')
        id_pedido = validated_data.pop('id_pedido')
        
        # Crear el objeto AportePedido sin los campos no definidos en el modelo
        aporte_pedido = AportePedido.objects.create(**validated_data)
        
        # Asignar los campos adicionales
        aporte_pedido.id_usuario = id_usuario
        aporte_pedido.fecha = fecha
        aporte_pedido.id_pedido = id_pedido
        aporte_pedido.save()
        
        return aporte_pedido

    def validate(self, data):
        cantidad = data.get('cantidad', None)
        if cantidad is not None and cantidad <= 0:
            raise serializers.ValidationError('La cantidad debe ser mayor a 0.')

        id_pedido = data.get('id_pedido', None)
        if id_pedido is not None and not Pedido.objects.filter(id_pedido=id_pedido.id_pedido).exists():
            raise serializers.ValidationError('El pedido referenciado no existe.')
        
        if id_pedido is None:
            raise serializers.ValidationError('Debe proporcionar id_pedido.')
        
        return data

class EstadopedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadopedido
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    id_obra = ObraSerializer()
    id_usuario = UsuarioSerializer()
    id_producto = ProductoSerializer()

    urgente_label = serializers.SerializerMethodField()

    class Meta:
        model = Pedido
        fields = '__all__'
        extra_fields = ['urgente_label']

    def get_urgente_label(self, obj):
        return obj.get_urgente_display()

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
        