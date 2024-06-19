from django.urls import path
from ProntaEntregaApp.views import *

urlpatterns = [
    path('', view=index, name='index'),
    path('register/', UserRegister.as_view(), name='user_register'),
    path('login/', UserLogin.as_view(), name='user_login'),
    path('userToken/<str:token>', UserByToken.as_view(), name='userToken'),
    path('profile/', UserPage.as_view(), name='profile'),
    path('user/', VerUsuarios.as_view(), name='users'),
    path('user/<str:email>', UserByEmail.as_view(), name='userEmail'),
    path('cambiar_contrasenia/', CambiarContrasenia.as_view(), name='change_password'),
    path('CambiarProducto/<int:pk>/', CambiarProducto.as_view(), name='CambiarProducto'),
    path('CambiarDetalleStock/<int:pk>/', CambiarDetalleStock.as_view(), name='CambiarDetalleStock'),
    path('stock/<int:categoria_id>/', VerStockYProducto.as_view(), name='ver_stock_producto'),
    path('tipo_documento/', verTipoDocumento.as_view(), name='ver_tipo_documento'),
    path('crear_casa/', CasaPost.as_view(), name='casa_post'),
    path('casa/', CasaGet.as_view(), name='casa_get'),
    path('editar_casa/<int:pk>/', EditarCasa.as_view(), name='casa_edit'),
    path('direcciones/', GetDirecciones.as_view(), name='direcciones_get'),
    path('crear_direccion/', CrearDirecciones.as_view(), name='direcciones_post'),
    path('direccion/<str:localidad>/<int:numero>/<str:calle>', GetDireccion.as_view(), name='direccion_get'),
    path('editar_direccion/<int:pk>/', EditarDirecciones.as_view(), name='direcciones_edit'),
    path('user/delete/<int:pk>/', UserDelete.as_view(), name='user_delete'),
    path('api/usuarios/update/<int:pk>/', UserUpdate.as_view(), name='user-update'),
    path('informacion_casas/', informacion_casas, name='informacion_casas'),
    path('asignar_usuario_a_casa/', asignar_usuario_a_casa, name='asignar_usuario_a_casa'),
]
