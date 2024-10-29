from django.core.management.base import BaseCommand
from ProntaEntregaApp.models import EntregaAporte,EstadoEntrega
from django.utils import timezone

class Command(BaseCommand):
    help = 'pasa las entregas de "en espera" a "en proceso" si llega su dia de entrega'

    def handle(self, *args, **kwargs):
        hoy =timezone.now().date()
        estado_pendiente = EstadoEntrega.objects.get(pk=2)
        estado_finalizado = EstadoEntrega.objects.get(pk=3)

        entregas_esperando = EntregaAporte.objects.filter(id_estadoEntrega = estado_pendiente)
        print("entregas:")
        print(entregas_esperando)
        print('----')

        for p in entregas_esperando:
            print(p.fechaEntrega)
            print(hoy)

            if p.fechaEntrega <= hoy:
                p.id_estadoEntrega = estado_finalizado
                p.save()
                print('a')
            else:
                print('b')