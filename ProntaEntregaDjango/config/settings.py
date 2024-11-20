from pathlib import Path
from dotenv import load_dotenv
from google.oauth2 import service_account
import os
import json
import base64

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
gcloud_credentials_base64 = os.getenv('GCLOUD_CREDENTIALS_BASE64')

if gcloud_credentials_base64 is None:
    raise ValueError("La variable de entorno GCLOUD_CREDENTIALS_BASE64 no está definida")

# Agrega el padding correcto a la cadena base64
missing_padding = len(gcloud_credentials_base64) % 4
if missing_padding != 0:
    gcloud_credentials_base64 += '=' * (4 - missing_padding)

# Decodifica la cadena base64
try:
    gcloud_credentials_json = base64.b64decode(gcloud_credentials_base64).decode('utf-8')
except Exception as e:
    raise ValueError(f"Error al decodificar la cadena base64: {e}")

# Carga las credenciales
try:
    gcloud_credentials = json.loads(gcloud_credentials_json)
except json.JSONDecodeError as e:
    raise ValueError(f"Error al decodificar el JSON: {e}")

GS_CREDENTIALS = service_account.Credentials.from_service_account_info(gcloud_credentials)

# Nombre del bucket
GS_BUCKET_NAME = 'bucket-django-pronta-entrega'

# Configuraciones de almacenamiento
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

# Control de acceso público opcional
GS_DEFAULT_ACL = 'publicRead'

# URL base para los medios
MEDIA_URL = f'https://storage.googleapis.com/bucket-django-pronta-entrega/media/'

# URL base para archivos estáticos
STATIC_URL = f'https://storage.googleapis.com/bucket-django-pronta-entrega/static/'

# Proyecto de Google Cloud
GS_PROJECT_ID = 'flawless-point-427320-h6'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', default='django-insecure-#&')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')

if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]
CORS_ALLOW_CREDENTIALS = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'ProntaEntregaApp'
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:8000",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:8000",
    "https://fat2024g3-frontend.onrender.com",
]

CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
DATABASES = {
    "default":{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('mysqldatabase'),
        'USER': os.getenv('mysqluser'),
        'PASSWORD': os.getenv('mysqlpassword'),
        'HOST': os.getenv('mysqlhost'),
        'PORT': os.getenv('mysqlport'),
    }
}

AUTH_USER_MODEL = 'ProntaEntregaApp.CustomUsuario'

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# STATIC_URL = f'https://storage.googleapis.com/{GS_BUCKET_NAME}/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)