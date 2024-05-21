from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginView.as_view() , name='login'),
    path('login', views.loginView.as_view() , name='login'),
    path('register', views.registerView.as_view() , name='register'),
    path('logout', views.logoutView.as_view() , name='logout'),
    path('user', views.userView.as_view() , name='user'),
]
