from rest_framework import serializers
from ProntaEntregaApp.models import *
from ProntaEntregaApp.serializers import *
from django.contrib.auth import authenticate

class DetalleofertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalleoferta
        fields = '__all__'

class EstadoofertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadooferta
        fields = '__all__'

class OfertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oferta
        fields = '__all__'