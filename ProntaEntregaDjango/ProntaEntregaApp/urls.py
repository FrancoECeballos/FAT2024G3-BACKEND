from django.urls import path
from . import views
from ProntaEntregaApp.views import *


urlpatterns = [    
    path('registro/', view=UserRegister, name='usuario_registro'),
    path('login/', view=UserLogin, name='usuario_login'),
    path('test/', view=test_token, name='test_token'),
]
