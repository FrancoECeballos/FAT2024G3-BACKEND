from rest_framework import serializers
from ProntaEntregaApp.models import *
from ProntaEntregaApp.serializers import *
from django.contrib.auth import authenticate

class TipousuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipousuario
        fields = '__all__'

class TipodocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipodocumento
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class UsuarioRegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
    def create (self, clean_data):
        user = Usuario.objects.create_user(
            clean_data['nombre'],
            clean_data['apellido'],
            clean_data['email'],
            clean_data['telefono'],
            clean_data['direccion'],
            clean_data['contrasena'],
            clean_data['tipousuario'],
            clean_data['tipodocumento']
        )
        user.save()
        return user

class UsuarioLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    contrasena = serializers.CharField()

    def checkUser(self, clean_data):
        user = authenticate(
            email=clean_data['email'],
            password=clean_data['contrasena']
        )
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        return user