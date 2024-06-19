from rest_framework import serializers
from ProntaEntregaApp.models import *
from ProntaEntregaApp.serializers.generalSerializers import *
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

class TipousuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipousuario
        fields = '__all__'

class TipodocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipodocumento
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    id_direccion = DireccionSerializer(many = False)
    id_tipousuario = TipousuarioSerializer(many = False)
    id_tipodocumento = TipodocumentoSerializer(many = False)
    
    class Meta:
        model = CustomUsuario
        fields = ['nombre', 'apellido', 'nombreusuario', 'password', 'documento', 'telefono', 'email', 'genero', 'id_direccion', 'id_tipousuario', 'id_tipodocumento', 'is_staff', 'is_superuser', 'is_active', 'is_verified']


class UsuarioUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUsuario
        fields = ['nombre', 'apellido', 'nombreusuario', 'documento', 'telefono', 'email', 'genero', 'imagen', 'id_direccion', 'id_tipousuario', 'id_tipodocumento']

    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.apellido = validated_data.get('apellido', instance.apellido)
        instance.nombreusuario = validated_data.get('nombreusuario', instance.nombreusuario)
        instance.documento = validated_data.get('documento', instance.documento)
        instance.telefono = validated_data.get('telefono', instance.telefono)
        instance.email = validated_data.get('email', instance.email)
        instance.genero = validated_data.get('genero', instance.genero)
        instance.imagen = validated_data.get('imagen', instance.imagen)
        instance.id_direccion = validated_data.get('id_direccion', instance.id_direccion)
        instance.id_tipousuario = validated_data.get('id_tipousuario', instance.id_tipousuario)
        instance.id_tipodocumento = validated_data.get('id_tipodocumento', instance.id_tipodocumento)
        instance.save()
        return instance


class UsuarioRegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUsuario
        fields = ['nombre', 'apellido', 'nombreusuario', 'password', 'documento', 'telefono', 'email', 'genero', 'imagen', 'id_direccion', 'id_tipousuario', 'id_tipodocumento']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        
        email = data.get('email', '').strip()
        username = data.get('nombreusuario', '').strip()
        password = data.get('password', '').strip()

        if not email or CustomUsuario.objects.filter(email=email).exists():
            raise ValidationError('choose another email')
        
        if not password or len(password) < 8:
            raise ValidationError('choose another password, min 8 characters')
        
        if not username:
            raise ValidationError('choose another username')
        
        return data

    def create(self, validated_data):
        user = CustomUsuario.objects.create_user(
            nombre=validated_data['nombre'],
            apellido=validated_data['apellido'],
            nombreusuario=validated_data['nombreusuario'],
            documento=validated_data['documento'],
            telefono=validated_data['telefono'],
            email=validated_data['email'],
            genero=validated_data['genero'],
            password=validated_data['password'],
            imagen='imagen',
            id_direccion=validated_data['id_direccion'],
            id_tipousuario=validated_data['id_tipousuario'],
            id_tipodocumento=validated_data['id_tipodocumento'],
        )
        return user


class UsuarioLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = CustomUsuario
        fields = ['email', 'password']
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(email=email, password=password)
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        return attrs
