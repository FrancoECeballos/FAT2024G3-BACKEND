from rest_framework import serializers
from ProntaEntregaApp.models import *
from ProntaEntregaApp.serializers import *
from django.contrib.auth import authenticate


class ObraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obra
        fields = ['id_obra', 'nombre', 'descripcion', 'id_organizacion', 'id_direccion', 'imagen']
        
    def validate_nombre(self, value):
        if Obra.objects.filter(nombre=value).exists():
            raise serializers.ValidationError("Ya existe una obra con este nombre")
        return value
    
    def create(self, validated_data):
        obra = Obra.objects.create_obra(
            nombre=validated_data.get('nombre'),
            descripcion=validated_data.get('descripcion'),
            id_organizacion=validated_data.get('id_organizacion'),
            id_direccion=validated_data.get('id_direccion'),
            imagen=validated_data.get('imagen')
        )
        return obra
    
class EditarObraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obra
        fields = ['id_obra', 'nombre', 'descripcion', 'id_organizacion', 'id_direccion']
    
    def create(self, validated_data):
        obra = Obra.objects.create_obra(
            nombre=validated_data.get('nombre'),
            descripcion=validated_data.get('descripcion'),
            id_organizacion=validated_data.get('id_organizacion'),
            id_direccion=validated_data.get('id_direccion')
        )
        return obra

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

class DetalleobrapedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalleobrapedido
        fields = '__all__'

class TransporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transporte
        fields = '__all__'

class DetalleobratransporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalleobratransporte
        fields = '__all__'

class ObraSerializer(serializers.ModelSerializer):
    id_direccion = DireccionSerializer()
    usuarios_registrados = serializers.SerializerMethodField()
    autos_registrados = serializers.SerializerMethodField()

    class Meta:
        model = Obra
        fields = ['id_obra', 'nombre', 'descripcion', 'id_organizacion', 'id_direccion', 'usuarios_registrados', "autos_registrados", 'imagen']

    def get_usuarios_registrados(self, obra):
        return obra.detalleobrausuario_set.count()
    
    def get_autos_registrados(self, obra):
        return obra.detalleobratransporte_set.count()
    
class DetalleobrausuarioSerializer(serializers.ModelSerializer):
    id_obra = serializers.PrimaryKeyRelatedField(queryset=Obra.objects.all())
    id_tipousuario = serializers.PrimaryKeyRelatedField(queryset=Tipousuario.objects.all())
    class Meta:
        model = Detalleobrausuario
        fields = '__all__'

    def validate(self, data):
        id_obra = data.get('id_obra')
        id_usuario = data.get('id_usuario')

        if Detalleobrausuario.objects.filter(id_obra=id_obra, id_usuario=id_usuario).exists():
            raise serializers.ValidationError("El usuario ya está registrado en esta obra.")
        
        return data
    
class CodigosDeVerificacionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CodigosDeVerificacion
        fields = '__all__'

class NotificacionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Notificacion
        fields = '__all__'

class DetalleObraTransporteSerializer():
    class Meta:
        model = Detalleobratransporte
        fields = '__all__'