from django.core.management.base import BaseCommand
from ProntaEntregaApp.models import Estadooferta,Oferta
from django.utils import timezone

class Command(BaseCommand):
    help = 'pasa las ofertas disponibles a vencidos si pasa su rango de tiempo establecido '

    def handle(self, *args, **kwargs):
        hoy =timezone.now().date()
        estado_pendiente = Estadooferta.objects.get(pk=1)
        estado_finalizado = Estadooferta.objects.get(pk=5)

        ofertas_dispo = Oferta.objects.filter(id_estadoOferta = estado_pendiente)
        print("ofertas:")
        print(ofertas_dispo)
        print('----')

        for o in ofertas_dispo:
            print(o.fechavencimiento)
            print(hoy)

            if o.fechavencimiento <= hoy:
                o.id_estadoOferta = estado_finalizado
                o.save()
                print('a')
            else:
                print('b')