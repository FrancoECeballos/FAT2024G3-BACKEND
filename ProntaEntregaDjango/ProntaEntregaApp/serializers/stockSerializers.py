from rest_framework import serializers
from ProntaEntregaApp.models import *
from ProntaEntregaApp.serializers import *
from ProntaEntregaApp.serializers.generalSerializers import ObraSerializer
from django.contrib.auth import authenticate

class UnidadmedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidadmedida
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class CategoriaprodutoSerializer(serializers.ModelSerializer):
    cantidad_productos = serializers.SerializerMethodField()
    id_categoria = CategoriaSerializer()

    class Meta:
        model = Categoriaproducto
        fields = ['id_categoriaproducto', 'nombre', 'descripcion', 'id_categoria', 'cantidad_productos']

    def get_cantidad_productos(self, obj):
        return Producto.objects.filter(id_categoriaproducto=obj).count()

class ProductoSerializer(serializers.ModelSerializer):
    id_categoriaproducto = CategoriaprodutoSerializer()
    id_unidadmedida = UnidadmedidaSerializer()

    class Meta:
        model = Producto
        fields = ['id_producto', 'nombre', 'descripcion', 'id_categoriaproducto', 'id_unidadmedida', 'imagen']

    def validate_id_categoriaproducto(self, value):
        if value is None:
            raise serializers.ValidationError("This field is required.")
        return value

    def validate_id_unidadmedida(self, value):
        if value is None:
            raise serializers.ValidationError("This field is required.")
        return value

class StockSerializer(serializers.ModelSerializer):
    id_obra = ObraSerializer()
    
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
        fields = ['id_detallestockproducto', 'titulo', 'descripcion', 'imagen', 'cantidad', 'cantidadUnidades', 'id_unidadmedida', 'id_producto', 'id_stock', 'multiplicacion']

    def get_multiplicacion(self, obj):
        cantidad = obj.cantidad if obj.cantidad else 0
        cantidad_unidades = obj.cantidadUnidades if obj.cantidadUnidades else 0
        return cantidad * cantidad_unidades

class CrearDetallestockproductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detallestockproducto
        fields = ['id_detallestockproducto','titulo','descripcion','imagen', 'cantidad', 'cantidadUnidades', 'id_unidadmedida', 'id_producto', 'id_stock']
        extra_kwargs = {
            'id_producto': {'required': True, 'allow_null': False},
            'id_stock': {'required': True, 'allow_null': False},
            'id_unidadmedida': {'required': True, 'allow_null': False},
            'cantidad': {'required': False, 'allow_null': True},
            'cantidadUnidades': {'required': False, 'allow_null': True},
        }

    def to_internal_value(self, data):
        internal_value = super().to_internal_value(data)
        internal_value['id_unidadmedida'] = Unidadmedida.objects.get(pk=data.get('id_unidadmedida'))
        internal_value['id_stock'] = Stock.objects.get(pk=data.get('id_stock'))
        internal_value['id_producto'] = Producto.objects.get(pk=data.get('id_producto'))
        return internal_value

    def validate(self, data):
        required_fields = ['id_producto', 'id_stock', 'id_unidadmedida']
        for field in required_fields:
            if field not in data or data[field] is None:
                raise serializers.ValidationError({field: 'Este campo es obligatorio y no puede ser nulo.'})
        return data

