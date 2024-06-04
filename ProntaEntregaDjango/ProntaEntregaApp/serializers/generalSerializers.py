from rest_framework import serializers
from ProntaEntregaApp.models import *
from ProntaEntregaApp.serializers import *
from django.contrib.auth import authenticate


class CasaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casa
        fields = ['nombre', 'descripcion', 'id_organizacion', 'id_direccion']

    def validate_nombre(self, value):
        # Verificar si ya existe una casa con el mismo nombre
        if Casa.objects.filter(nombre=value).exists():
            raise serializers.ValidationError("Ya existe una casa con este nombre")
        return value
    
    def create(self, validated_data):
        casa = Casa.objects.create_casa(
            nombre=validated_data.get('nombre'),
            descripcion=validated_data.get('descripcion'),
            id_organizacion=validated_data.get('id_organizacion'),
            id_direccion=validated_data.get('id_direccion')
        )
        return casa


class DetallecasausuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detallecasausuario
        fields = '__all__'

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'
    
class OrganizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizacion
        fields = '__all__'

class TransporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transporte
        fields = '__all__'

    