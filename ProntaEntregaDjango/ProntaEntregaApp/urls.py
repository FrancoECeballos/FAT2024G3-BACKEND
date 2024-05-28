from django.urls import path
from . import views
from ProntaEntregaApp.views import *


urlpatterns = [
    path('', view=index, name='index'),
    path('register/', UserRegister.as_view(), name='user_register'),
    path('login/', UserLogin.as_view(), name='user_login'),
    path('test/', TestToken.as_view(), name='test_token'),
    path('cambiar_contrasena/', view=CambiarContraseña, name='change_password'),
    path('user/', view=ver_usuarios, name='users'),
]
