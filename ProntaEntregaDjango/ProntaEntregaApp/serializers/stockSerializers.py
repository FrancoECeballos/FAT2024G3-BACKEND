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
        fields = ['id_stock', 'id_casa']

    def get_usuarios_registrados(self, stock):
        return stock.id_casa.detallecasausuario_set.count()

class DetallestockproductoSerializer(serializers.ModelSerializer):
    id_stock = StockSerializer()
    id_producto = ProductoSerializer()
    id_unidadmedida = UnidadmedidaSerializer()
    
    class Meta:
        model = Detallestockproducto
        fields = ['id_detallestockproducto','cantidad','cantidadUnidades','id_stock','id_producto','id_unidadmedida']

