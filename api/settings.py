"""
Django settings for api project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import django_heroku
import environ
import dj_database_url

# import cloudinary


env= environ.Env(

    DEBUG=(bool, False)
)

# cloudinary.config( 
#   cloud_name = env('CLOUD_NAME'), 
#   api_key = env('API_KEY'), 
#   api_secret = env('API_SECRET') 
# )



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates/')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')
# SECRET_KEY = "b'\xf1^c\xe9\xc4'"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')
# DEBUG = True

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
# ALLOWED_HOSTS = []


# Application definition

SHARED_APPS = (
    'django_tenants', # mandatory, should always be before any django app
    'shop', # you must list the app where your tenant model resides in
    'users', 

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
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
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',

    # your tenant-specific apps
    'customers',
    'orders',
    'sales',
    'transaction',
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
        },
    },
]

WSGI_APPLICATION = 'api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
   
    'default': env.db(),
    # 'default': {
    #     'ENGINE': 'django_tenants.postgresql_backend',
    #     'NAME': 'zeus_api', 
    #     'USER': 'postgres', 
    #     'PASSWORD': 'welcome@1',
    #     'HOST': '127.0.0.1', 
    #     'PORT': '5432',
    # }
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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_DIRS =[os.path.join(BASE_DIR, 'static'),]
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = "django_tenants.staticfiles.storage.TenantStaticFilesStorage"
MULTITENANT_RELATIVE_STATIC_ROOT = ""
MEDIA_URL = os.path.join(BASE_DIR, 'media/')
MEDIA_ROOT ='/media/'
DEFAULT_FILE_STORAGE = "django_tenants.files.storage.TenantFileSystemStorage"
MULTITENANT_RELATIVE_MEDIA_ROOT = ""
# config = locals()
# django_heroku.settings(config, databases=False)

# conn_max_age = config.get('CONN_MAX_AGE', 600) # Used in django-heroku
# config['DATABASES'] = {
#     'default': dj_database_url.parse(
#         os.environ['DATABASE_URL'],
#         engine='django_tenants.postgresql_backend',
#         conn_max_age=conn_max_age,
#         ssl_require=True
#         )
# }
