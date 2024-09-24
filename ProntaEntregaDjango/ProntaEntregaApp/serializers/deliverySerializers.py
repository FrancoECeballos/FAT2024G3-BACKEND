from rest_framework import serializers
from ProntaEntregaApp.models import *
from ProntaEntregaApp.serializers import *
from ProntaEntregaApp.serializers.requestSerializers import *
from ProntaEntregaApp.serializers.offerSerializers import *
from ProntaEntregaApp.serializers.generalSerializers import *
from django.contrib.auth import authenticate

class EntregaSerializer(serializers.ModelSerializer):
    id_pedido = PedidoSerializer()
    id_oferta = OfertaSerializer()

    class Meta:
        model = Entrega
        fields = '__all__'

class CreateEntregaSerializer(serializers.ModelSerializer):
    id_pedido = serializers.PrimaryKeyRelatedField(queryset=Pedido.objects.all())
    id_oferta = serializers.PrimaryKeyRelatedField(queryset=Oferta.objects.all())
    fechaCreacion = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"])

    class Meta:
        model = Entrega
        fields = '__all__'


class EstadoEntregaSerializer(serializers.ModelSerializer):

    class Meta:
        model = EstadoEntrega
        fields = '__all__'


class EntregaAporteSerializer(serializers.ModelSerializer):
    id_entrega = EntregaSerializer()
    id_aportePedido = AportePedidoSerializer()
    id_aporteOferta = DetalleofertaSerializer()
    id_transporte = TransporteSerializer()
    id_estadoEntrega = EstadoEntregaSerializer()

    class Meta:
        model = EntregaAporte
        fields = '__all__'

class CreateEntregaAporteSerializer(serializers.ModelSerializer):
    id_entrega = serializers.PrimaryKeyRelatedField(queryset=Entrega.objects.all())
    id_aportePedido = serializers.PrimaryKeyRelatedField(queryset=AportePedido.objects.all())
    id_aporteOferta = serializers.PrimaryKeyRelatedField(queryset=AportePedido.objects.all())
    id_transporte = serializers.PrimaryKeyRelatedField(queryset=Transporte.objects.all())
    id_estadoEntrega = serializers.PrimaryKeyRelatedField(queryset=EstadoEntrega.objects.all())
    fechaCreacion = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"])
    fechaEntrega = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"])

    class Meta:
        model = Entrega
        fields = '__all__'