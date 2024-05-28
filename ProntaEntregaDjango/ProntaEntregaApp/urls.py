from django.urls import path
from ProntaEntregaApp.views import *


urlpatterns = [
    path('', view=index, name='index'),
    path('register/', UserRegister.as_view(), name='user_register'),
    path('login/', UserLogin.as_view(), name='user_login'),
    path('test/', TestToken.as_view(), name='test_token'),
    path('cambiar_contrasenia/', CambiarContrasenia.as_view(), name='change_password'),
    path('stock/<int:categoria_id>/', VerStockYProducto.as_view(), name='ver_stock_producto'),
    path('ver_usuarios/', VerUsuarios.as_view(), name='ver_usuarios'),
]
