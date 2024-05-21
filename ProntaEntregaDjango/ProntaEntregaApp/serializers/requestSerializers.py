from rest_framework import serializers
from ProntaEntregaApp.models import *
from ProntaEntregaApp.serializers import *
from django.contrib.auth import authenticate

class DetallepedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detallepedido
        fields = '__all__'

class EstadopedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadopedido
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'