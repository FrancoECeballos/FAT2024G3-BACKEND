from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib import  messages
from django.views import View
from ProntaEntregaApp.models import *

# Create your views here.

from django.shortcuts import render

class loginView(generics.GenericApiView):
    def get(self, request: HttpRequest, *args, **kwargs):
        return Response ({"message": "Hello, world!"})
