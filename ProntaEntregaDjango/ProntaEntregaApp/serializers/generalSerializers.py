from rest_framework import serializers
from ProntaEntregaApp.models import *
from ProntaEntregaApp.serializers import *
from django.contrib.auth import authenticate


class CasaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casa
        fields = ['id_casa', 'nombre', 'descripcion', 'id_organizacion', 'id_direccion']
        
    def validate_nombre(self, value):
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
    
class EditarCasaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casa
        fields = ['id_casa', 'nombre', 'descripcion', 'id_organizacion', 'id_direccion']
    
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

    def create(self, validated_data):
        direccion = Direccion.objects.create_direccion(
            localidad=validated_data.get('localidad'),
            numero=validated_data.get('numero'),
            calle=validated_data.get('calle'),
        )
        return direccion
    
class OrganizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizacion
        fields = '__all__'

class TransporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transporte
        fields = '__all__'

    