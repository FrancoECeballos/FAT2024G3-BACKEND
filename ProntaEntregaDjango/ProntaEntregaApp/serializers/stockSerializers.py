from rest_framework import serializers
from ProntaEntregaApp.models import *
from ProntaEntregaApp.serializers import *
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

class DetallestockproductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detallestockproducto
        fields = ['id_detallestockproducto','cantidad','id_stock','id_producto']

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id_producto', 'nombre', 'descripcion', 'id_categoriaproducto', 'id_unidadmedida']

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
    class Meta:
        model = Stock
        fields = '__all__'
