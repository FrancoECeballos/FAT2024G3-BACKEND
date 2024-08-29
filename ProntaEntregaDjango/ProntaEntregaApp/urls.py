from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ProntaEntregaApp.views import *
from . import views

urlpatterns = [
    path('', view=index, name='index'),

    path('getNotificacion/<int:pk>', GetNotificacionesDeUser.as_view(), name='GetNotificacionesDeUsr'),
    path('PostNotificacion/', PostNotificacion.as_view(), name='PostNotificacion'),
    
    path('user/', VerUsuarios.as_view(), name='users'),
    path('user/<str:email>', UserByEmail.as_view(), name='userEmail'),
    path('user/id/<int:pk>/', UserByID.as_view(), name='userID'),
    path('user/obra/', AllUsersByObra.as_view(), name='ver_all_user_obra'),
    path('user/obra/null/', AllUsersByObra_null.as_view(), name='AllUsersByObra_null'),
    path('obra/user/<str:token>/', ObraByUser.as_view(), name='ver_obra_user'),
    path('obra/nouser/<str:token>/', ObraSinUsuario.as_view(), name='AllUsersByObra_null'),
    path('user/obra/<int:id_obra>/', UserByObra.as_view(), name='ver_user_obra'),
    
    path('direcciones/', GetDirecciones.as_view(), name='direcciones_get'),
    path('crear_direccion/', CrearDirecciones.as_view(), name='direcciones_post'),
    path('direccion/<int:pk>', GetDireccion.as_view(), name='direccion_get'),
    path('editar_direccion/<int:pk>/', EditarDirecciones.as_view(), name='direcciones_edit'),
    
    path('organizaciones/', GetOrganizaciones.as_view(), name='organizaciones_get'),
    path('crear_organizacion/', CrearOrganizaciones.as_view(), name='organizaciones_post'),
    path('editar_organizacion/<int:pk>/', EditarOrganizaciones.as_view(), name='organizaciones_edit'),
    
    path('tipo_documento/', GetTipoDocumento.as_view(), name='ver_tipo_documento'),
    path('crear_tipo_documento/', CrearTipoDocumento.as_view(), name='crear_tipo_documento'),
    path('editar_tipo_documento/<int:pk>/', EditarTipoDocumento.as_view(), name='editar_tipo_documento'),

    path('tipo_usuario/', GetTipoUsuario.as_view(), name='ver_tipo_usuario'),
    path('crear_tipo_usuario/', CrearTipoUsuario.as_view(), name='crear_tipo_usuario'),
    path('editar_tipo_usuario/<int:pk>/', EditarTipoUsuario.as_view(), name='editar_tipo_usuario'),

    path('register/', UserRegister.as_view(), name='user_register'),
    path('login/', UserLogin.as_view(), name='user_login'),
    path('userToken/<str:token>/', UserByToken.as_view(), name='userToken'),
    path('cambiar_contrasenia/', CambiarContrasenia.as_view(), name='change_password'),        
    path('CambiarContrasenia_open/<str:email>/', CambiarContrasenia_open.as_view(), name='CambiarContrasenia_open'), ##no abrir sin consultar que es esto

    path('obra/', GetObra.as_view(), name='obra_get'),
    path('obra/<int:pk>/', GetObraByID.as_view(), name='obra_get_id'),
    path('crear_obra/', CrearObra.as_view(), name='obra_post'),
    path('editar_obra/<int:pk>', EditarObra.as_view(), name='obra_edit'),

    path('stock/', GetStock.as_view(), name='ver_stock'),
    path('stock/<int:id_obra>/', GetStockByID.as_view(), name='ver_stock_id'),
    path('stock/<int:categoria_id>/', VerStockYProducto.as_view(), name='ver_stock_producto'),
    path('GetProductoByStock/<int:id_stock>/<int:id_categoria>/', GetProductoByStock.as_view(), name='GetProductoByStock'),
    path('crear_stock/', CrearStock.as_view(), name='crear_stock'),
    path('editar_stock/<int:pk>/', EditarStock.as_view(), name='editar_stock'),

    path('categoria/', GetCategoria.as_view(), name='ver_categoria'),
    path('categoria/<int:id_categoria>/', GetCategoriaByID.as_view(), name='ver_categoria_id'),
    path('crear_categoria/', CrearCategoria.as_view(), name='crear_categoria'),
    path('editar_categoria/<int:pk>/', EditarCategoria.as_view(), name='editar_categoria'),

    path('productos/', GetProductos.as_view(), name='ver_producto'),
    path('producto/<int:pk>/', GetProductoById.as_view(), name='ver_producto_id'),
    path('crear_productos/', CrearProductos.as_view(), name='crear_producto'),
    path('editar_producto/<int:pk>/', EditarProducto.as_view(), name='editar_producto'),

    path('pedido/', GetPedido.as_view(), name='ver_pedido'),
    path('crear_pedido/', CrearPedido.as_view(), name='crear_pedido'),
    path('eliminar_pedido/<int:pk>/', DeletePedido.as_view(), name='eliminar_pedido'),
    path('editar_pedido/<int:pk>/', EditarPedido.as_view(), name='editar_pedido'),
    path('eliminar_pedido/<int:pk>/', DeletePedido.as_view(), name='eliminar_pedido'),
    path('estado_pedido/', GetEstadoPedido.as_view(), name='ver_estado_pedido'),
    path('crear_estado_pedido/', CrearEstadoPedido.as_view(), name='crear_estado_pedido'),
    path('editar_estado_pedido/<int:pk>/', EditarEstadoPedido.as_view(), name='editar_estado_pedido'),
    path('aporte_pedido/', GetAportePedido.as_view(), name='ver_detalle_pedido'),
    path('crear_aporte_pedido/', CrearAportePedido.as_view(), name='crear_aporte_pedido'),
    path('editar_aporte_pedido/<int:pk>/', EditarAportePedido.as_view(), name='editar_aporte_pedido'),
    path('get_pedido_by_user/<str:token>/', GetPedidosByUser.as_view(), name='get_pedido_by_user'),
    path('get_pedido_for_admin/', GetPedidosForAdmin.as_view(), name='get_pedido_for_admin'),
    path('detalle_pedido/', GetDetalleobrapedido.as_view(), name='ver_detalle_pedido'),
    path('crear_detalle_pedido/', CrearDetalleobrapedido.as_view(), name='crear_detalle_pedido'),
    path('delete_detalle_pedido/<int:pk>/', DeleteDetalleobrapedido.as_view(), name='editar_detalle_pedido'),

    path('oferta/', GetOferta.as_view(), name='ver_oferta'),
    path('GetOfertaSimilar/<int:id_obra>/<int:id_producto>/', GetOfertaSimilar.as_view(), name='GetOfertaSimilar'),
    path('oferta/<int:pk>/', GetOfertaById.as_view(), name='ver_oferta_por_id'),
    path('crear_oferta/', CrearOferta.as_view(), name='crear_oferta'),
    path('editar_oferta/<int:pk>/', EditarOferta.as_view(), name='editar_oferta'),
    path('estado_oferta/', GetEstadoOferta.as_view(), name='ver_estado_oferta'),
    path('crear_estado_oferta/', CrearEstadoOferta.as_view(), name='crear_estado_oferta'),
    path('editar_estado_oferta/<int:pk>/', EditarEstadoOferta.as_view(), name='editar_estado_oferta'),
    path('aporte_oferta/', GetAporteOferta.as_view(), name='ver_detalle_oferta'),
    path('crear_detalle_oferta/', CrearDetalleOferta.as_view(), name='crear_detalle_oferta'),
    path('editar_detalle_oferta/<int:pk>/', EditarDetalleOferta.as_view(), name='editar_detalle_oferta'),

    path('transporte/', GetTransporte.as_view(), name='ver_transporte'),
    path('transporte/<int:id_obra>/', GetTransporteByObra.as_view(), name='ver_transporte_obra'),
    path('crear_transporte/', CrearTransporte.as_view(), name='crear_transporte'),
    path('editar_transporte/<int:pk>/', EditarTransporte.as_view(), name='editar_transporte'),
    path('eliminar_detalle_transporte/<int:id_obra>/<int:id_transporte>/', EliminarTransporte.as_view(), name='eliminar_transporte'),
    path('detalle_transporte/', GetDetalleobratransporte.as_view(), name='ver_detalle_transporte'),
    path('crear_detalle_transporte/', PostDetalleobratransporte.as_view(), name='crear_detalle_transporte'),

#---------------------------------------------------------------------------------------
    path('profile/', UserPage.as_view(), name='profile'),
    path('CambiarStock/<int:pk>/', CambiarStock.as_view(), name='CambiarStock'),
    path('CambiarProducto/<int:pk>/', CambiarProducto.as_view(), name='CambiarProducto'),
    path('CambiarDetalleStock/<int:pk>/', CambiarDetalleStock.as_view(), name='CambiarDetalleStock'),
    path('PostStock/', PostStock.as_view(), name='PostStock'),
    path('PostProducto/', PostProducto.as_view(), name='PostProducto'),
    path('DeleteStock/<int:pk>/', DeleteStock.as_view(), name='DeleteStock'),
    path('DeleteProducto/<int:pk>/', DeleteProducto.as_view(), name='DeleteProducto'),
    path('DeleteDetallestockproducto/<int:pk>/', DeleteDetallestockproducto.as_view(), name='DeleteDetallestockproducto'),
    path('user/delete/<str:email>/', UserDelete.as_view(), name='user_delete'),
    path('user/Verificar/<int:pk>/', Verificar.as_view(), name='Verificar'),
    path('user/update/<str:token>/', UserUpdate.as_view(), name='user-update'),
    path('user/updateEmail/<str:email>/', UserUpdateEmail.as_view(), name='user-update-email'),
    path('categoria/delete/<int:pk>/', CategoriaDelete.as_view(), name='categoria_delete'),
    path('categoria/post', CategoriaPost.as_view(), name='categoria_post'),
    path('user/obras/post/', PostDetalleObraUsuario.as_view(), name='user-obras-post'),
    path('user/obrasEmail/<str:email>/', GetObrasAsignadasByEmail.as_view(), name='user-obrasEmail'),
    path('user/obrasToken/<str:token>/', GetObrasAsignadasByToken.as_view(), name='user-obrasToken'),
    path('user/stockEmail/<str:email>/', GetStockAsignadoByEmail.as_view(), name='user-stockEmail'),
    path('user/stockToken/<str:token>/', GetStockAsignadoByToken.as_view(), name='user-stockToken'),
    path('user/obras/delete/<int:pk>/', DeleteDetalleObraUsuario.as_view(), name='user-obras-delete'),
    path('obra/<int:id_stock>/categoria_producto/<str:id_categoriaproducto>/<int:id_categoria>/', ProductosPorCategoriaYObraView.as_view(), name='productos-por-categoria-y-obra'),
    path('detallestockproducto/<int:id_detallestockproducto>/', UpdateDetallestockproductoView.as_view(), name='detallestockproducto-update'),
    
    path('AddDetallestockproducto/', PostDetallestockproducto.as_view(), name='AddDetallestockproducto'),
    path('SubtractDetallestockproducto/', RestarDetallestockproducto.as_view(), name='SubtractDetallestockproducto'),

    path('detallestock/', DetallestockproductoView.as_view(), name='detallestockproducto'),
    path('detallestockproducto/', CreateDetallestockproductoView.as_view(), name='detallestockproducto-create'),
    path('restardetallestockproducto/', RestarDetallestockproducto.as_view(), name='RestarDetallestockproducto'),
    path('gdetallestockproducto/<int:id_detallestockproducto>/', GetDetallestockproductoView.as_view(), name='detallestockproducto-get'),
    path('GetDetallestockproducto_Total/<int:id_stock>/<int:id_categoria>/', GetDetallestockproducto_Total.as_view(), name='GetDetallestockproducto_Total'),
    path('ddetallestockproducto/<int:id_detallestockproducto>/', DeleteDetallestockproductoView.as_view(), name='detallestockproducto-delete'),
    path('GetUsuariosPorPedido/<int:id_pedido>/', GetUsuariosPorPedido.as_view(), name='GetUsuariosPorPedido'),

    path('informe-pedidos-pdf/', PedidoInformePDFView.as_view(), name='informe-pedidos-pdf'),
    path('informe-stock-pdf/<int:id_producto>/<int:id_stock>/<str:token>/', StockInformePDFView.as_view(), name='informe-stock-pdf'),

    path('GetProductosPorCategoriaExcluidos/<int:id_categoria>/', GetProductosPorCategoriaExcluidos.as_view(), name='getProductosPorCategoriaExcluidos'),
    path('GetDetallesProductoObra/<int:id_producto>/<int:id_stock>/', GetDetallesProductoObra.as_view(), name='GetDetallesProductoObra'),
    path('GetTotalProductoObra/<int:id_stock>/<int:id_producto>/', GetCantidadTotalProductoObra.as_view(), name='GetTotalProductoObra'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)