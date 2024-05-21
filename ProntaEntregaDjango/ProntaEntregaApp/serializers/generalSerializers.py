from rest_framework import serializers
from ProntaEntregaApp.models import *
from ProntaEntregaApp.serializers import *
from django.contrib.auth import authenticate


class CasaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casa
        fields = '__all__'

class DetallecasausuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detallecasausuario
        fields = '__all__'

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'
    
class OrganizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizacion
        fields = '__all__'

class TransporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transporte
        fields = '__all__'

    