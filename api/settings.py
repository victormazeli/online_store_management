
"""
Django settings for api project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates/')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')
# SECRET_KEY = 'wiejiwiwrwiriw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get('DEBUG', default=0))
# DEBUG = True

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOST').split(" ")
# ALLOWED_HOSTS = []



# Application definition

SHARED_APPS = (
    'django_tenants', # mandatory, should always be before any django app
    'shop', # you must list the app where your tenant model resides in
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'users',
    'django_filters',
    'rest_framework',
    'rest_framework.authtoken', 
    'djoser',  
    'bootstrap4',

)

TENANT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_filters',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser', 

    # your tenant-specific apps
    'products',
    'sales',
    'orders',
    'customers',
   
)

INSTALLED_APPS = list(SHARED_APPS) + [app for app in TENANT_APPS if app not in SHARED_APPS]

SITE_ID = 1

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES':[
         'rest_framework.authentication.TokenAuthentication',
         'rest_framework.authentication.SessionAuthentication'
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
 
    
}

TENANT_MODEL = "shop.Shop" # app.Model
TENANT_DOMAIN_MODEL = "shop.Domain"
AUTH_USER_MODEL = 'users.CustomUser'
MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        'loaders': [
                "django_tenants.template.loaders.filesystem.Loader",  # Must be first
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
        },
    },
]

WSGI_APPLICATION = 'api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {

    # 'default': {
    #      'ENGINE': 'django_tenants.postgresql_backend',
    #      'NAME': 'postgres', 
    #      'USER': 'postgres', 
    #      'PASSWORD': 'welcome@1',
    #      'HOST': 'localhost', 
    #      'PORT': '5432',
    #  }
   
     'default': {
         'ENGINE': os.environ.get('DATABASE_ENGINE'),
         'NAME': os.environ.get('DATABASE_NAME'), 
         'USER': os.environ.get('DATABASE_USER'), 
         'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
         'HOST': os.environ.get('DATABASE_HOST'), 
         'PORT': os.environ.get('DATABASE_PORT'),
     }
}

DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)


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

STATICFILES_FINDERS = [
    "django_tenants.staticfiles.finders.TenantFileSystemFinder",  # Must be first
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
]

MULTITENANT_TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, "tenants/%s/templates"),
]

MULTITENANT_STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "tenants/%s/static" ),
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

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_STORAGE = "django_tenants.staticfiles.storage.TenantStaticFilesStorage"
DEFAULT_FILE_STORAGE = "django_tenants.files.storage.TenantFileSystemStorage"

REWRITE_STATIC_URLS = True
