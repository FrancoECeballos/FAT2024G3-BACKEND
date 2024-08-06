from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ProntaEntregaApp.views import *
from . import views

urlpatterns = [
    path('', view=index, name='index'),

    path('getNotificacion/<int:pk>', GetNotificacionesDeUser.as_view(), name='GetNotificacionesDeUsr'),
    
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
    path('userToken/<str:token>', UserByToken.as_view(), name='userToken'),
    path('cambiar_contrasenia/', CambiarContrasenia.as_view(), name='change_password'),        
    path('CambiarContrasenia_open/<int:pk>/', CambiarContrasenia_open.as_view(), name='CambiarContrasenia_open'), ##no abrir sin consultar que es esto

    path('obra/', GetObra.as_view(), name='obra_get'),
    path('obra/<int:pk>', GetObraByID.as_view(), name='obra_get_id'),
    path('crear_obra/', CrearObra.as_view(), name='obra_post'),
    path('editar_obra/<int:pk>', EditarObra.as_view(), name='obra_edit'),

    path('unidad_medida/', GetUnidadMedida.as_view(), name='ver_unidad_medida'),
    path('crear_unidad_medida/', CrearUnidadMedida.as_view(), name='crear_unidad_medida'),
    path('editar_unidad_medida/<int:pk>/', EditarUnidadMedida.as_view(), name='editar_unidad_medida'),

    path('stock/', GetStock.as_view(), name='ver_stock'),
    path('stock/<int:id_obra>/', GetStockByID.as_view(), name='ver_stock_id'),
    path('stock/<int:categoria_id>/', VerStockYProducto.as_view(), name='ver_stock_producto'),
    path('crear_stock/', CrearStock.as_view(), name='crear_stock'),
    path('editar_stock/<int:pk>/', EditarStock.as_view(), name='editar_stock'),

    path('categoria/', GetCategoria.as_view(), name='ver_categoria'),
    path('crear_categoria/', CrearCategoria.as_view(), name='crear_categoria'),
    path('editar_categoria/<int:pk>/', EditarCategoria.as_view(), name='editar_categoria'),

    path('categoria_producto/', GetCategoriaProducto.as_view(), name='ver_categoria_producto'),
    path('categoria_producto/<int:id_categoria>/', GetCategoriaProductoByCategoria.as_view(), name='ver_categoria_producto_by_categoria'),
    path('crear_categoria_producto/', CrearCategoriaProducto.as_view(), name='crear_categoria_producto'),
    path('editar_categoria_producto/<int:pk>/', EditarCategoriaProducto.as_view(), name='editar_categoria_producto'),

    path('productos/', GetProductos.as_view(), name='ver_producto'),
    path('producto/<int:pk>/', GetProductoById.as_view(), name='ver_producto_id'),
    path('crear_productos/', CrearProductos.as_view(), name='crear_producto'),
    path('editar_producto/<int:pk>/', EditarProducto.as_view(), name='editar_producto'),

    path('pedido/', GetPedido.as_view(), name='ver_pedido'),
    path('crear_pedido/', CrearPedido.as_view(), name='crear_pedido'),
    path('editar_pedido/<int:pk>/', EditarPedido.as_view(), name='editar_pedido'),
    path('estado_pedido/', GetEstadoPedido.as_view(), name='ver_estado_pedido'),
    path('crear_estado_pedido/', CrearEstadoPedido.as_view(), name='crear_estado_pedido'),
    path('editar_estado_pedido/<int:pk>/', EditarEstadoPedido.as_view(), name='editar_estado_pedido'),
    path('detalle_pedido/', GetDetallePedido.as_view(), name='ver_detalle_pedido'),
    path('crear_detalle_pedido/', CrearDetallePedido.as_view(), name='crear_detalle_pedido'),
    path('editar_detalle_pedido/<int:pk>/', EditarDetallePedido.as_view(), name='editar_detalle_pedido'),

    path('oferta/', GetOferta.as_view(), name='ver_oferta'),
    path('crear_oferta/', CrearOferta.as_view(), name='crear_oferta'),
    path('editar_oferta/<int:pk>/', EditarOferta.as_view(), name='editar_oferta'),
    path('estado_oferta/', GetEstadoOferta.as_view(), name='ver_estado_oferta'),
    path('crear_estado_oferta/', CrearEstadoOferta.as_view(), name='crear_estado_oferta'),
    path('editar_estado_oferta/<int:pk>/', EditarEstadoOferta.as_view(), name='editar_estado_oferta'),
    path('detalle_oferta/', GetDetalleOferta.as_view(), name='ver_detalle_oferta'),
    path('crear_detalle_oferta/', CrearDetalleOferta.as_view(), name='crear_detalle_oferta'),
    path('editar_detalle_oferta/<int:pk>/', EditarDetalleOferta.as_view(), name='editar_detalle_oferta'),

    path('transporte/', GetTransporte.as_view(), name='ver_transporte'),
    path('crear_transporte/', CrearTransporte.as_view(), name='crear_transporte'),
    path('editar_transporte/<int:pk>/', EditarTransporte.as_view(), name='editar_transporte'),

#---------------------------------------------------------------------------------------
    path('profile/', UserPage.as_view(), name='profile'),
    path('user/', VerUsuarios.as_view(), name='users'),
    path('user/<str:email>', UserByEmail.as_view(), name='userEmail'),
    path('user/id/<int:pk>/', UserByID.as_view(), name='userID'),
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
    path('categorias-productos/<int:id_stock>/', CategoriasProductosView.as_view(), name='categorias-productos'),
    path('obra/<int:id_stock>/categoria_producto/<str:id_categoriaproducto>/<int:id_categoria>/', ProductosPorCategoriaYObraView.as_view(), name='productos-por-categoria-y-obra'),
    path('detallestockproducto/<int:id_detallestockproducto>/', UpdateDetallestockproductoView.as_view(), name='detallestockproducto-update'),
    
    path('AddDetallestockproducto/', PostDetallestockproducto.as_view(), name='AddDetallestockproducto'),
    path('SubtractDetallestockproducto/', RestarDetallestockproducto.as_view(), name='SubtractDetallestockproducto'),

    path('detallestock/', DetallestockproductoView.as_view(), name='detallestockproducto'),
    path('detallestockproducto/', CreateDetallestockproductoView.as_view(), name='detallestockproducto-create'),
    path('restardetallestockproducto/', RestarDetallestockproducto.as_view(), name='RestarDetallestockproducto'),
    path('gdetallestockproducto/<int:id_detallestockproducto>/', GetDetallestockproductoView.as_view(), name='detallestockproducto-get'),
    path('ddetallestockproducto/<int:id_detallestockproducto>/', DeleteDetallestockproductoView.as_view(), name='detallestockproducto-delete'),
    path('catprod_obra/<int:id_categoria>/', CategoriaProductosPorCategoria.as_view(), name='detallestockproducto-categoria'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)