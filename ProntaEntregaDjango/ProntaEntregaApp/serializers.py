from rest_framework import serializers
from ProntaEntregaApp.models import *

class CasaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casa
        fields = '__all__'

class CategoriaprodutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoriaproducto
        fields = '__all__'

class DetallecasausuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detallecasausuario
        fields = '__all__'

class DetalleofertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalleoferta
        fields = '__all__'

class DetallepedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detallepedido
        fields = '__all__'

class DetallestockproductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detallestockproducto
        fields = '__all__'

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'

class EstadoofertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadooferta
        fields = '__all__'

class EstadopedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadopedido
        fields = '__all__'

class OfertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oferta
        fields = '__all__'
    
class OrganizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizacion
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class TipousuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipousuario
        fields = '__all__'

class TransporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transporte
        fields = '__all__'

class UnidadmedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidadmedida
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'