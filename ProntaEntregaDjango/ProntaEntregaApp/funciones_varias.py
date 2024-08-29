from ProntaEntregaApp.models import *
from ProntaEntregaApp.serializers import *
from ProntaEntregaApp.serializers.requestSerializers import *
from ProntaEntregaApp.serializers.offerSerializers import *

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

def lista_oferta_con_progreso(ofertas):
    all = []

    for p in ofertas:
        serializer = OfertaSerializer(p)

        total = 0
        aportes = AporteOferta.objects.filter(id_oferta = p.id_oferta)

        for a in aportes:
            total = total + a.cantidad

        s = serializer.data
        s.update({"progreso":total})
        all.append(s)
    return all