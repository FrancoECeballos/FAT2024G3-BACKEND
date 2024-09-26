from django.core.management.base import BaseCommand
from ProntaEntregaApp.models import *
from ProntaEntregaApp.serializers.stockSerializers import *
import random

class Command(BaseCommand):
    help = 'ejemplo de comando custom'

    def handle(self, *args, **kwargs):
        print('lol')
        p = CategoriaSerializer(data = {"nombre": "piedra"+random.randint(1, 100).__str__(),"descripcion" : "piedra"})
        
        if p.is_valid():
            print('ok')
            p.save()
        else:
            print(p.errors)

