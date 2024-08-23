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
    class Meta:
        model = Pedido
        fields = ['id_pedido', 'fechainicio', 'fechavencimiento', 'id_obra', 'id_usuario', 'cantidad', 'urgente', 'id_producto', 'id_estadoPedido']
        extra_kwargs = {
            'id_obra': {'required': True, 'allow_null': False},
            'id_usuario': {'required': True, 'allow_null': False},
            'cantidad': {'required': True, 'allow_null': False},
            'urgente': {'required': True, 'allow_null': False},
            'id_producto': {'required': True, 'allow_null': False},
            'id_estadoPedido': {'required': True, 'allow_null': False},
        }

    def validate(self, data):
        required_fields = ['id_obra', 'id_usuario', 'cantidad', 'urgente', 'id_producto', 'id_estadoPedido']
        for field in required_fields:
            if field not in data or data[field] is None:
                raise serializers.ValidationError({field: 'Este campo es obligatorio y no puede ser nulo.'})
        return data

    def to_internal_value(self, data):
        internal_value = super().to_internal_value(data)
        internal_value['id_obra'] = Obra.objects.get(pk=data.get('id_obra'))
        internal_value['id_usuario'] = CustomUsuario.objects.get(pk=data.get('id_usuario'))
        internal_value['id_producto'] = Producto.objects.get(pk=data.get('id_producto'))
        internal_value['id_estadoPedido'] = Estadopedido.objects.get(pk=data.get('id_estadoPedido'))
        return internal_value

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation   