from rest_framework import serializers
from ProntaEntregaApp.models import *
from ProntaEntregaApp.serializers.stockSerializers import *
from django.contrib.auth import authenticate

class EstadopedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadopedido
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class DetallepedidoSerializer(serializers.ModelSerializer):
    id_pedido = PedidoSerializer(many=False)
    id_estadopedido = EstadopedidoSerializer(many=False)
    id_producto = ProductoSerializer(many=False)

    class Meta:
        model = Detallepedido
        fields = '__all__'