from rest_framework import serializers
from ProntaEntregaApp.models import *
from ProntaEntregaApp.serializers import *
from django.contrib.auth import authenticate

class UnidadmedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidadmedida
        fields = '__all__'

class CategoriaprodutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoriaproducto
        fields = '__all__'

class DetallestockproductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detallestockproducto
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'
