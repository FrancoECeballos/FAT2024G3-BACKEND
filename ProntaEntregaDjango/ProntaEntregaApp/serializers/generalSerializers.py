from rest_framework import serializers
from ProntaEntregaApp.models import *
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
        fields = ['id_obra', 'nombre', 'descripcion', 'id_organizacion', 'id_direccion', 'imagen']
    
    def create(self, validated_data):
        obra = Obra.objects.create_obra(
            nombre=validated_data.get('nombre'),
            descripcion=validated_data.get('descripcion'),
            id_organizacion=validated_data.get('id_organizacion'),
            id_direccion=validated_data.get('id_direccion'),
            imagen=validated_data.get('imagen')
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

class CreateDetalleobrapedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalleobrapedido
        fields = ['id_stock', 'id_pedido']
    
    def create(self, validated_data):
        detalle = Detalleobrapedido.objects.create(
            id_stock=validated_data.get('id_stock'),
            id_pedido=validated_data.get('id_pedido')
        )
        return detalle
    
    def validate(self, data):
        required_fields = ['id_stock', 'id_pedido']
        for field in required_fields:
            if field not in data or data[field] is None:
                raise serializers.ValidationError({field: 'Este campo es obligatorio y no puede ser nulo.'})
        return data

    def to_internal_value(self, data):
        internal_value = super().to_internal_value(data)
        internal_value['id_stock'] = Stock.objects.get(pk=data.get('id_stock'))
        internal_value['id_pedido'] = Pedido.objects.get(pk=data.get('id_pedido'))
        return internal_value

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation

class TransporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transporte
        fields = ['id_transporte', 'imagen', 'marca', 'modelo', 'patente', 'kilometraje']

    def create(self, validated_data):
        auto = Transporte.objects.crear_transporte(
            imagen=validated_data['imagen'],
            marca=validated_data['marca'],
            modelo=validated_data['modelo'],
            patente=validated_data['patente'],
            kilometraje=validated_data['kilometraje']
        )
        return auto

class crearTransporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transporte
        fields = ['id_transporte', 'imagen', 'marca', 'modelo', 'patente', 'kilometraje']

    def create(self, validated_data):
        auto = Transporte.objects.crear_transporte(
            imagen=validated_data['imagen'],
            marca=validated_data['marca'],
            modelo=validated_data['modelo'],
            patente=validated_data['patente'],
            kilometraje=validated_data['kilometraje']
        )
        return auto
    
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
    
class CrearObraSerializer(serializers.ModelSerializer):
    id_direccion = serializers.PrimaryKeyRelatedField(queryset=Direccion.objects.all())

    class Meta:
        model = Obra
        fields = '__all__'
    
    
class DetalleobrausuarioSerializer(serializers.ModelSerializer):
    id_obra = serializers.PrimaryKeyRelatedField(queryset=Obra.objects.all())
    id_usuario = serializers.PrimaryKeyRelatedField(queryset=CustomUsuario.objects.all())
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

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        fecha_ingreso = instance.fechaingreso.strftime("%d/%m/%Y")
        representation['fechaingreso'] = fecha_ingreso
        return representation
    
class CodigosDeVerificacionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CodigosDeVerificacion
        fields = '__all__'

class NotificacionSerializer(serializers.ModelSerializer):
    fecha_creacion = serializers.SerializerMethodField()

    class Meta:
        model = Notificacion
        fields = '__all__'

    def get_fecha_creacion(self, notificacion):
        if notificacion.fecha_creacion:
            return notificacion.fecha_creacion.strftime("%d/%m/%Y")
        return None
    
class CrearNotificacionSerializer(serializers.ModelSerializer):
    id_usuario = serializers.PrimaryKeyRelatedField(queryset=CustomUsuario.objects.all())
    id_obra = serializers.PrimaryKeyRelatedField(queryset=Obra.objects.all())
    fecha_creacion = serializers.SerializerMethodField()

    class Meta:
        model = Notificacion
        fields = '__all__'

    def get_fecha_creacion(self, notificacion):
        if notificacion.fecha_creacion:
            return notificacion.fecha_creacion.strftime("%d/%m/%Y")
        return None

class DetalleObraTransporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalleobratransporte
        fields = '__all__'
