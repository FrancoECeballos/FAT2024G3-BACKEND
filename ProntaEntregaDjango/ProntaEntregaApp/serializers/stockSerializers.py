from rest_framework import serializers
from ProntaEntregaApp.models import *
from ProntaEntregaApp.serializers import *
from ProntaEntregaApp.serializers.generalSerializers import CasaSerializer
from django.contrib.auth import authenticate

class UnidadmedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidadmedida
        fields = '__all__'

class CategoriaprodutoSerializer(serializers.ModelSerializer):
    cantidad_productos = serializers.SerializerMethodField()

    class Meta:
        model = Categoriaproducto
        fields = ['nombre', 'cantidad_productos']

    def get_cantidad_productos(self, obj):
        return Producto.objects.filter(id_categoriaproducto=obj).count()

class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = ['id_producto', 'nombre', 'descripcion', 'id_categoriaproducto']

    # Optionally, you can add extra validation for foreign key fields
    def validate_id_categoriaproducto(self, value):
        if value is None:
            raise serializers.ValidationError("This field is required.")
        return value

    def validate_id_unidadmedida(self, value):
        if value is None:
            raise serializers.ValidationError("This field is required.")
        return value

class StockSerializer(serializers.ModelSerializer):
    id_casa = CasaSerializer()
    
    class Meta:
        model = Stock
        fields = '__all__'

class DetallestockproductoSerializer(serializers.ModelSerializer):
    id_unidadmedida = UnidadmedidaSerializer()
    id_stock = StockSerializer()
    id_producto = ProductoSerializer()
    multiplicacion = serializers.SerializerMethodField()

    class Meta:
        model = Detallestockproducto
        fields = ['id_detallestockproducto', 'cantidad', 'cantidadUnidades', 'id_unidadmedida', 'id_producto', 'id_stock', 'multiplicacion']
    
    def get_multiplicacion(self, obj):
        cantidad = obj.cantidad if obj.cantidad else 0
        cantidad_unidades = obj.cantidadUnidades if obj.cantidadUnidades else 0
        return cantidad * cantidad_unidades

class CrearDetallestockproductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detallestockproducto
        fields = ['id_detallestockproducto', 'cantidad', 'cantidadUnidades', 'id_unidadmedida', 'id_producto', 'id_stock']
        extra_kwargs = {
            'id_producto': {'required': True, 'allow_null': False},
            'id_stock': {'required': True, 'allow_null': False},
            'id_unidadmedida': {'required': True, 'allow_null': False},
            'cantidad': {'required': False, 'allow_null': True},
            'cantidadUnidades': {'required': False, 'allow_null': True},
        }

    def validate(self, data):
        required_fields = ['id_producto', 'id_stock', 'id_unidadmedida']
        for field in required_fields:
            if field not in data or data[field] is None:
                raise serializers.ValidationError({field: 'Este campo es obligatorio y no puede ser nulo.'})
        return data
        fields = ['id_detallestockproducto','cantidad','cantidadUnidades','id_stock','id_producto','id_unidadmedida']

