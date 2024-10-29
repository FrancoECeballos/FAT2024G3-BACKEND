from rest_framework import serializers
from ProntaEntregaApp.models import *
from ProntaEntregaApp.serializers.generalSerializers import ObraSerializer
from ProntaEntregaApp.serializers.userSerializers import UsuarioSerializer
from ProntaEntregaApp.serializers.stockSerializers import ProductoSerializer

class EstadoofertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadooferta
        fields = '__all__'

class OfertaSerializer(serializers.ModelSerializer):
    id_obra = ObraSerializer()
    id_usuario = UsuarioSerializer()
    id_estadoOferta = EstadoofertaSerializer()
    id_producto = ProductoSerializer()
    id_estadoOferta = EstadoofertaSerializer()

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

class DetalleofertaSerializer(serializers.ModelSerializer):
    id_oferta = OfertaSerializer()
    id_usuario = UsuarioSerializer()
    id_obra = ObraSerializer()

    class Meta:
        model = AporteOferta
        fields = '__all__'

class CrearDetalleofertaSerializer(serializers.ModelSerializer):
    id_oferta = serializers.PrimaryKeyRelatedField(queryset=Oferta.objects.all())
    id_usuario = serializers.PrimaryKeyRelatedField(queryset=CustomUsuario.objects.all())
    id_obra = serializers.PrimaryKeyRelatedField(queryset=Obra.objects.all())
    fechaAportado = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"])

    class Meta:
        model = AporteOferta
        fields = '__all__'