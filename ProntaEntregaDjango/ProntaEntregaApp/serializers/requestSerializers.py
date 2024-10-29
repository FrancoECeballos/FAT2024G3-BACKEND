from rest_framework import serializers
from ProntaEntregaApp.models import *
from ProntaEntregaApp.serializers.stockSerializers import *
from ProntaEntregaApp.serializers.generalSerializers import ObraSerializer
from ProntaEntregaApp.serializers.userSerializers import UsuarioSerializer

class EstadopedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadopedido
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    id_obra = ObraSerializer()
    id_usuario = UsuarioSerializer()
    id_producto = ProductoSerializer()
    id_estadoPedido = EstadopedidoSerializer()

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

class AportePedidoSerializer(serializers.ModelSerializer):
    id_pedido = PedidoSerializer()
    id_usuario = UsuarioSerializer()
    id_obra = ObraSerializer()
    
    class Meta:
        model = AportePedido
        fields = '__all__'

class CreateAportePedidoSerializer(serializers.ModelSerializer):
    id_pedido = serializers.PrimaryKeyRelatedField(queryset=Pedido.objects.all())
    id_usuario = serializers.PrimaryKeyRelatedField(queryset=CustomUsuario.objects.all())
    id_obra = serializers.PrimaryKeyRelatedField(queryset=Obra.objects.all())
    fechaAportado = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"])

    class Meta:
        model = AportePedido
        fields = '__all__'