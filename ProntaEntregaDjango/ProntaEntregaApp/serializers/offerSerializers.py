from rest_framework import serializers
from ProntaEntregaApp.models import *
from ProntaEntregaApp.serializers import *
from ProntaEntregaApp.serializers.generalSerializers import ObraSerializer
from ProntaEntregaApp.serializers.userSerializers import UsuarioSerializer
from ProntaEntregaApp.serializers.stockSerializers import ProductoSerializer
from django.contrib.auth import authenticate

class DetalleofertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AporteOferta
        fields = '__all__'

    def validate(self, data):
        cantidad = data.get('cantidad', None)
        if cantidad is not None and cantidad <= 0:
            raise serializers.ValidationError('La cantidad debe ser mayor a 0.')

        id_oferta = data.get('id_oferta', None)
        if id_oferta is not None and not Oferta.objects.filter(id_oferta=id_oferta.id_oferta).exists():
            raise serializers.ValidationError('El pedido referenciado no existe.')
        
        if id_oferta is None:
            raise serializers.ValidationError('debe proporcionar id_oferta.')

        return data

class EstadoofertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadooferta
        fields = '__all__'

class OfertaSerializer(serializers.ModelSerializer):
    id_obra = ObraSerializer()
    id_usuario = UsuarioSerializer()
    id_estadoOferta = EstadoofertaSerializer()
    id_producto = ProductoSerializer()

    class Meta:
        model = Oferta
        fields = '__all__'

class CrearOfertaSerializer(serializers.ModelSerializer):
    id_obra = serializers.PrimaryKeyRelatedField(queryset=Obra.objects.all())
    id_usuario = serializers.PrimaryKeyRelatedField(queryset=CustomUsuario.objects.all())
    id_estadoOferta = serializers.PrimaryKeyRelatedField(queryset=Estadooferta.objects.all())
    id_producto = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all())
    fechainicio = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"])
    fechavencimiento = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"])

    class Meta:
        model = Oferta
        fields = '__all__'