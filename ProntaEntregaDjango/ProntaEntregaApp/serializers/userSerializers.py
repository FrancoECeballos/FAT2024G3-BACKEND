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
        fields = ['nombre', 'apellido', 'nombreusuario', 'password', 'documento', 'telefono', 'email', 'id_direccion', 'id_tipousuario', 'id_tipodocumento']


    def create(self, validated_data):
        user = Usuario.objects.create_user(
            nombre=validated_data['nombre'],
            apellido=validated_data['apellido'],
            nombreusuario=validated_data['nombreusuario'],
            documento=validated_data['documento'],
            telefono=validated_data['telefono'],
            email=validated_data['email'],
            password=validated_data['password'],
            id_direccion=validated_data['id_direccion'],
            id_tipousuario=validated_data['id_tipousuario'],
            id_tipodocumento=validated_data['id_tipodocumento'],
        )
        return user


class UsuarioLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = Usuario
        fields = ['email', 'password']
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(email=email, password=password)
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        return attrs
