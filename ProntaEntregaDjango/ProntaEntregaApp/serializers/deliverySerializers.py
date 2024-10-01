from rest_framework import serializers
from ProntaEntregaApp.models import Entrega, EntregaAporte, EstadoEntrega, Pedido, Oferta, AportePedido, AporteOferta, Transporte
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
    id_pedido = serializers.PrimaryKeyRelatedField(queryset=Pedido.objects.all(), required=False, allow_null=True)
    id_oferta = serializers.PrimaryKeyRelatedField(queryset=Oferta.objects.all(), required=False, allow_null=True)
    fechaCreacion = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"], required=False)

    class Meta:
        model = Entrega
        fields = '__all__'

    def validate(self, data):
        # Ensure at least one of 'id_pedido' or 'id_oferta' is provided
        if not data.get('id_pedido') and not data.get('id_oferta'):
            raise serializers.ValidationError("You must provide either 'id_pedido' or 'id_oferta'.")
        return data

class CreateEntregaAporteSerializer(serializers.ModelSerializer):
    id_entrega = serializers.PrimaryKeyRelatedField(queryset=Entrega.objects.all())
    id_aportePedido = serializers.PrimaryKeyRelatedField(queryset=AportePedido.objects.all(), required=False, allow_null=True)
    id_aporteOferta = serializers.PrimaryKeyRelatedField(queryset=AporteOferta.objects.all(), required=False, allow_null=True)
    id_estadoEntrega = serializers.PrimaryKeyRelatedField(queryset=EstadoEntrega.objects.all())

    class Meta:
        model = EntregaAporte
        fields = '__all__'