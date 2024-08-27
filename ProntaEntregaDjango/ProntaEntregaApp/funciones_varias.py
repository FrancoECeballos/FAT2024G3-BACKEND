from ProntaEntregaApp.models import *
from ProntaEntregaApp.serializers import *
from ProntaEntregaApp.serializers.requestSerializers import *

def lista_pedido_con_progreso(pedidos):
    all = []

    for p in pedidos:
        serializer = PedidoSerializer(p)

        total = 0
        aportes = AportePedido.objects.filter(id_pedido = p.id_pedido)

        for a in aportes:
            total = total + a.cantidad

        s = serializer.data
        s.update({"progreso":total})
        all.append(s)
    return all