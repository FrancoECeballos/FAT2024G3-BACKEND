from pathlib import Path
from dotenv import load_dotenv
from google.oauth2 import service_account
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# Configurar credenciales de Google Cloud Storage
GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    os.path.join(BASE_DIR, 'credentials/my-gcloud-credentials.json')
)

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
SECRET_KEY = 'django-insecure-z(fv!69g=(omoc8se6)lz*v#2nta9!5rjk$6uuz++x(i=b81=i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

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
]

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
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
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
    "default": {
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
