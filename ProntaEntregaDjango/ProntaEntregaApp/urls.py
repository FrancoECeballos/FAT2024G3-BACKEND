from django.urls import path
from ProntaEntregaApp.views import *


urlpatterns = [
    path('', view=index, name='index'),
    path('register/', UserRegister.as_view(), name='user_register'),
    path('login', UserLogin.as_view(), name='user_login'),
    path('test/', TestToken.as_view(), name='test_token'),
    path('profile/', UserPage.as_view(), name='profile'),
    path('user/', VerUsuarios.as_view(), name='users'),
    path('user/<pk>', UserByID.as_view(), name='userID'),
    path('cambiar_contrasenia/', CambiarContrasenia.as_view(), name='change_password'),
    path('stock/<int:categoria_id>/', VerStockYProducto.as_view(), name='ver_stock_producto'),
]
