from django.core.management.base import BaseCommand
from ProntaEntregaApp.models import *
from django.utils import timezone

class Command(BaseCommand):
    help = 'borra notificaciones con una semana de antiguedad'

    def handle(self, *args, **kwargs):
        hoy =timezone.now().date()
        notifs = Notificacion.objects.all()
        for x in notifs:
            if x.fecha_creacion < hoy:
                print(x.fecha_creacion)
                x.delete()
