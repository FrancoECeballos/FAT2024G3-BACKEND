from rest_framework import serializers
from ProntaEntregaApp.models import *
from ProntaEntregaApp.serializers.stockSerializers import *
from ProntaEntregaApp.serializers.generalSerializers import CasaSerializer
from ProntaEntregaApp.serializers.userSerializers import UsuarioSerializer
from django.contrib.auth import authenticate

class EstadopedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadopedido
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    id_casa = CasaSerializer()
    id_usuario = UsuarioSerializer()

    class Meta:
        model = Pedido
        fields = '__all__'

class DetallepedidoSerializer(serializers.ModelSerializer):
    id_pedido = PedidoSerializer(many=False)
    id_estadopedido = EstadopedidoSerializer(many=False)
    
    class Meta:
        model = AportePedido
        fields = '__all__'