from django.core.management.base import BaseCommand
from ProntaEntregaApp.models import *
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'borra notificaciones con una semana de antiguedad'

    def handle(self, *args, **kwargs):
        one_week_ago = timezone.now().date() - timedelta(weeks=1)
        notifs = Notificacion.objects.all()

        for x in notifs:
            if x.fecha_creacion < one_week_ago:
                print(x.fecha_creacion)
                x.delete()
