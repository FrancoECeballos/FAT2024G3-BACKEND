from rest_framework import serializers
from ProntaEntregaApp.models import *
from ProntaEntregaApp.serializers import *
from ProntaEntregaApp.serializers.generalSerializers import ObraSerializer
from ProntaEntregaApp.serializers.userSerializers import UsuarioSerializer
from django.contrib.auth import authenticate


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    id_categoria = CategoriaSerializer()
    unidadmedida = serializers.SerializerMethodField()

    class Meta:
        model = Producto
        fields = ['id_producto', 'nombre', 'descripcion', 'id_categoria', 'imagen', 'unidadmedida']

    def get_unidadmedida(self, obj):
        return obj.get_unidadmedida_display()

    def validate_id_categoria(self, value):
        if value is None:
            raise serializers.ValidationError("This field is required.")
        return value
    
class CreateProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id_producto', 'nombre', 'descripcion', 'id_categoria', 'imagen', 'unidadmedida']
        extra_kwargs = {
            'id_categoria': {'required': True, 'allow_null': False},
            'nombre': {'required': True, 'allow_null': False},
            'descripcion': {'required': True, 'allow_null': False},
            'unidadmedida': {'required': True, 'allow_null': False},
        }

    def create(self, validated_data):
        product = Producto.objects.create(
            nombre=validated_data['nombre'],
            descripcion=validated_data['descripcion'],
            id_categoria=validated_data['id_categoria'],
            imagen=validated_data['imagen'],
            unidadmedida=validated_data['unidadmedida'],
        )
        return product

    def validate(self, data):
        required_fields = ['id_categoria', 'nombre', 'descripcion', 'unidadmedida']
        for field in required_fields:
            if field not in data or data[field] is None:
                raise serializers.ValidationError({field: 'Este campo es obligatorio y no puede ser nulo.'})
        return data

    def to_internal_value(self, data):
        internal_value = super().to_internal_value(data)
        internal_value['id_categoria'] = Categoria.objects.get(pk=data.get('id_categoria'))
        return internal_value

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation

class StockSerializer(serializers.ModelSerializer):
    id_obra = ObraSerializer()
    
    class Meta:
        model = Stock
        fields = '__all__'

class DetallestockproductoSerializer(serializers.ModelSerializer):
    id_stock = StockSerializer()
    id_producto = ProductoSerializer()
    id_usuario = UsuarioSerializer()

    class Meta:
        model = Detallestockproducto
        fields = ['id_detallestockproducto', 'checkpoint', 'fecha_creacion', 'cantidad', 'id_producto', 'id_stock', 'id_usuario']

class DspSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detallestockproducto
        fields = ['id_detallestockproducto', 'checkpoint', 'fecha_creacion', 'cantidad', 'id_producto', 'id_stock', 'id_usuario']

class CrearDetallestockproductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detallestockproducto
        fields = ['id_detallestockproducto', 'checkpoint', 'fecha_creacion', 'cantidad', 'id_producto', 'id_stock', 'id_usuario']
        extra_kwargs = {
            'id_producto': {'required': True, 'allow_null': False},
            'id_stock': {'required': True, 'allow_null': False},
            'id_usuario': {'required': True, 'allow_null': False},
            'cantidad': {'required': False, 'allow_null': True},
        }

    def to_internal_value(self, data):
        internal_value = super().to_internal_value(data)
        internal_value['id_stock'] = Stock.objects.get(pk=data.get('id_stock'))
        internal_value['id_producto'] = Producto.objects.get(pk=data.get('id_producto'))
        internal_value['id_usuario'] = CustomUsuario.objects.get(pk=data.get('id_usuario'))
        return internal_value

    def validate(self, data):
        required_fields = ['id_producto', 'id_stock', 'id_usuario']
        for field in required_fields:
            if field not in data or data[field] is None:
                raise serializers.ValidationError({field: 'Este campo es obligatorio y no puede ser nulo.'})
        return data
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        fecha_creacion = instance.fecha_creacion
        if fecha_creacion:
            representation['fecha_creacion'] = fecha_creacion.strftime('%d/%m/%Y %H:%M:%S')
        return representation
