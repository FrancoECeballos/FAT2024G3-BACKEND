from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from ProntaEntregaApp.models import *

def custom_validation(data):
    email = data['email'].strip()
    username = data['nombreusuario'].strip()
    password = data['contrasenia'].strip()
    ##
    if not email or Usuario.objects.filter(email=email).exists():
        raise ValidationError('choose another email')
    ##
    if not password or len(password) < 8:
        raise ValidationError('choose another password, min 8 characters')
    ##
    if not username:
        raise ValidationError('choose another username')
    return data


def validate_email(data):
    email = data['email'].strip()
    if not email:
        raise ValidationError('an email is needed')
    return True

def validate_username(data):
    username = data['nombreusuario'].strip()
    if not username:
        raise ValidationError('choose another username')
    return True

def validate_password(data):
    password = data['contrasenia'].strip()
    if not password:
        raise ValidationError('a password is needed')
    return True