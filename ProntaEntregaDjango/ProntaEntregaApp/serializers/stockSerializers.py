from rest_framework import serializers
from ProntaEntregaApp.models import *
from ProntaEntregaApp.serializers import *
from ProntaEntregaApp.serializers.generalSerializers import ObraSerializer
from django.contrib.auth import authenticate


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    id_categoria = CategoriaSerializer()

    class Meta:
        model = Producto
        fields = ['id_producto', 'nombre', 'descripcion', 'id_categoria', 'imagen']

    def validate_id_categoria(self, value):
        if value is None:
            raise serializers.ValidationError("This field is required.")
        return value

class StockSerializer(serializers.ModelSerializer):
    id_obra = ObraSerializer()
    
    class Meta:
        model = Stock
        fields = '__all__'

class DetallestockproductoSerializer(serializers.ModelSerializer):
    id_stock = StockSerializer()
    id_producto = ProductoSerializer()
    multiplicacion = serializers.SerializerMethodField()

    class Meta:
        model = Detallestockproducto
        fields = ['id_detallestockproducto', 'titulo', 'descripcion', 'cantidad', 'id_producto', 'id_stock', 'multiplicacion']

    def get_multiplicacion(self, obj):
        cantidad = obj.cantidad if obj.cantidad else 0
        return cantidad

class CrearDetallestockproductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detallestockproducto
        fields = ['id_detallestockproducto', 'titulo', 'descripcion','chackpoint','fecha_creacion', 'cantidad', 'id_producto', 'id_stock']
        extra_kwargs = {
            'id_producto': {'required': True, 'allow_null': False},
            'id_stock': {'required': True, 'allow_null': False},
            'cantidad': {'required': False, 'allow_null': True},
        }

    def to_internal_value(self, data):
        internal_value = super().to_internal_value(data)
        internal_value['id_stock'] = Stock.objects.get(pk=data.get('id_stock'))
        internal_value['id_producto'] = Producto.objects.get(pk=data.get('id_producto'))
        return internal_value

    def validate(self, data):
        required_fields = ['id_producto', 'id_stock']
        for field in required_fields:
            if field not in data or data[field] is None:
                raise serializers.ValidationError({field: 'Este campo es obligatorio y no puede ser nulo.'})
        return data
