from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginView.as_view() , name='login'),
    path('login', views.loginView.as_view() , name='login'),
]
