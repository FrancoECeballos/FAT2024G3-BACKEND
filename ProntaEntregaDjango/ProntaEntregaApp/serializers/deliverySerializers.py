from rest_framework import serializers
from ProntaEntregaApp.models import Entrega, EntregaAporte, EstadoEntrega, Pedido, Oferta, AportePedido, Transporte
from ProntaEntregaApp.serializers.requestSerializers import PedidoSerializer, AportePedidoSerializer
from ProntaEntregaApp.serializers.offerSerializers import DetalleofertaSerializer, OfertaSerializer
from ProntaEntregaApp.serializers.generalSerializers import TransporteSerializer

class EstadoEntregaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoEntrega
        fields = '__all__'

class EntregaAporteSerializer(serializers.ModelSerializer):
    id_aportePedido = AportePedidoSerializer()
    id_aporteOferta = DetalleofertaSerializer()
    id_transporte = TransporteSerializer()
    id_estadoEntrega = EstadoEntregaSerializer()

    class Meta:
        model = EntregaAporte
        fields = '__all__'

class EntregaSerializer(serializers.ModelSerializer):
    id_pedido = PedidoSerializer()
    id_oferta = OfertaSerializer()
    entrega_aportes = serializers.SerializerMethodField()

    class Meta:
        model = Entrega
        fields = '__all__'

    def get_entrega_aportes(self, obj):
        entrega_aportes = EntregaAporte.objects.filter(id_entrega=obj.id_entrega)
        return EntregaAporteSerializer(entrega_aportes, many=True).data

class CreateEntregaSerializer(serializers.ModelSerializer):
    id_pedido = serializers.PrimaryKeyRelatedField(queryset=Pedido.objects.all())
    id_oferta = serializers.PrimaryKeyRelatedField(queryset=Oferta.objects.all())
    fechaCreacion = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"])

    class Meta:
        model = Entrega
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
        model = EntregaAporte
        fields = '__all__'