"""
Django settings for djtrustlab project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#od(y&w@)tfbeksjl03az4tubnulo#lps7=si^pk%@ghn1%l=i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# FORCE_SCRIPT_NAME = '/trustlab'
# Application definition

INSTALLED_APPS = [
    'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'trustlab.apps.TrustlabConfig',
    'rest_framework',
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

ROOT_URLCONF = 'djtrustlab.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR + '/trustlab/templates/', ],
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

WSGI_APPLICATION = 'djtrustlab.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'NAME': 'trustlab-dev',
    #     'ENGINE': 'sql_server.pyodbc',
    #     'HOST': 'stratus.informatik.tu-chemnitz.de',
    #     'PORT': '1433',
    #     'USER': 'trustlab-dev',
    #     'PASSWORD': 'dev@17092019#',
    #     'OPTIONS': {
    #             'driver': 'ODBC Driver 17 for SQL Server',
    #     }
    # },
    'default': {
        'NAME': os.path.join(BASE_DIR, 'trustlab.sqlite3'),
        'ENGINE': 'django.db.backends.sqlite3',
        # 'HOST': 'stratus.informatik.tu-chemnitz.de',
        # 'PORT': '1433',
        # 'USER': 'trustlab-dev',
        # 'PASSWORD': 'dev@17092019#',
        # 'OPTIONS': {
        #         'driver': 'ODBC Driver 17 for SQL Server',
        # }
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'trustlab/static'),
]

STATIC_URL = '/static/'
STATIC_ROOT = 'deploy/static'

MEDIA_URL = '/media/'
MEDIA_ROOT = 'deploy/uploads'

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
#X_FRAME_OPTIONS = 'DENY'
X_FRAME_OPTIONS = 'SAMEORIGIN'

# Configurations for Django channels with Redis
ASGI_APPLICATION = "djtrustlab.routing.application"
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
    # For local testing
    # "default": {
    #     "BACKEND": "channels.layers.InMemoryChannelLayer"
    # },
}

