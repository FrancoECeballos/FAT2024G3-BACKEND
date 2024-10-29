from django.core.management.base import BaseCommand
from ProntaEntregaApp.models import Pedido,Estadopedido
from django.utils import timezone

class Command(BaseCommand):
    help = 'pasa los pedidos disponibles a vencidos si pasa su rango de tiempo establecido'

    def handle(self, *args, **kwargs):
        hoy =timezone.now().date()
        estado_pendiente = Estadopedido.objects.get(pk=1)
        estado_finalizado = Estadopedido.objects.get(pk=3)

        pedidos_dispo = Pedido.objects.filter(id_estadoPedido = estado_pendiente)
        print("pedidos:")
        print(pedidos_dispo)
        print('----')

        for p in pedidos_dispo:
            print(p.fechavencimiento)
            print(hoy)

            if p.fechavencimiento < hoy:
                p.id_estadoPedido = estado_finalizado
                p.save()
                print('a')
            else:
                print('b')