from rest_framework import serializers
from ProntaEntregaApp.models import *
from ProntaEntregaApp.serializers import *
from ProntaEntregaApp.serializers.generalSerializers import CasaSerializer
from ProntaEntregaApp.serializers.userSerializers import UsuarioSerializer
from ProntaEntregaApp.serializers.stockSerializers import ProductoSerializer
from django.contrib.auth import authenticate

class DetalleofertaSerializer(serializers.ModelSerializer):
   
    
    class Meta:
        model = AporteOferta
        fields = '__all__'

class EstadoofertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadooferta
        fields = '__all__'

class OfertaSerializer(serializers.ModelSerializer):
    id_casa = CasaSerializer()
    id_usuario = UsuarioSerializer()
    id_estadooferta = EstadoofertaSerializer()
    id_producto = ProductoSerializer()

    class Meta:
        model = Oferta
        fields = '__all__'