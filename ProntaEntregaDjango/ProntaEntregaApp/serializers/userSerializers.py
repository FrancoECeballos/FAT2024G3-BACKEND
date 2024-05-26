from rest_framework import serializers
from ProntaEntregaApp.models import *
from ProntaEntregaApp.serializers.generalSerializers import *
from django.contrib.auth import authenticate

class TipousuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipousuario
        fields = '__all__'

class TipodocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipodocumento
        fields = '__all__'


class UsuarioRegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'nombreusuario', 'contrasenia', 'documento', 'telefono', 'email', 'id_direccion', 'id_tipousuario', 'id_tipodocumento']


    def create(self, validated_data):
        user = Usuario.objects.create_user(
            nombre=validated_data['nombre'],
            apellido=validated_data['apellido'],
            nombreusuario=validated_data['nombreusuario'],
            documento=validated_data['documento'],
            telefono=validated_data['telefono'],
            email=validated_data['email'],
            contrasenia=validated_data['contrasenia'],
            id_direccion=validated_data['id_direccion'],
            id_tipousuario=validated_data['id_tipousuario'],
            id_tipodocumento=validated_data['id_tipodocumento'],
        )
        return user


class UsuarioLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    contrasenia = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        contrasenia = attrs.get('contrasenia')

        user = authenticate(email=email, password=contrasenia)
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        return attrs