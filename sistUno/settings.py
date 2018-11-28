"""
Django settings for sistUno project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from django.urls import reverse_lazy
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y)oz^1$9&!lb873q_!1pvf-7tu+$lal-3$$yz$44i$20w3qqyi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Propio
    'sistUno',
    'apps.deposito',
    'apps.pago',
    'apps.solicitud',
    'apps.usuario',
    'apps.home',
    'apps.testimonio',
    'apps.articulo',
    'apps.reset',
    'apps.notificacion',
    'apps.general',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sistUno.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'sistUno.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        # nube
        'ENGINE': 'mysql_cymysql',
        'NAME': 'admin_ayudammm',
        'USER': 'admin_ayudammm',
        'PASSWORD': 'sQhhhzqrfu',
        'HOST': '138.197.36.187',
        'PORT': '3306'

        # local
        # 'ENGINE': 'mysql_cymysql',
        # 'NAME': 'proyectodb',
        # 'USER': 'usuario_proyecto',
        # 'PASSWORD': '1234',
        # 'HOST': 'localhost',
        # 'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'es-pe'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True
# USE_L10N = False

USE_TZ = True

# DATE_FORMAT = "d-m-Y"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS=(os.path.join(BASE_DIR, 'static'),)

MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'apps/media')
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')




# LOGIN Y LOGOUT

LOGOUT_REDIRECT_URL=reverse_lazy('home:index')

#CORREO ELECTRONICO
EMAIL_USE_TLS=True
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=25
# EMAIL_HOST_USER='mariayobeth@gmail.com'
EMAIL_HOST_USER='fincomun.info@gmail.com'
EMAIL_HOST_PASSWORD='fincomun@info.com'
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
