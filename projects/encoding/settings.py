# -*- coding: utf-8 -*-

from unipath import Path
BASE_DIR = Path(__file__).ancestor(3)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9y5-0^fl!b=v67i5hot8rus()sr4wmwofk-c8)te*t7=maux^-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    #'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.main',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'projects.encoding.urls'

WSGI_APPLICATION = 'projects.encoding.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'encoding_catalogar',
        'USER':'encoding_admin',
        'PASSWORD' : 'admin2015',
        'HOST':'65.19.143.2',
        'PORT' : '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-ec'

TIME_ZONE = 'America/Guayaquil'

USE_I18N = True

USE_L10N = True

USE_TZ = True

"""
    BASE_DIR = ...../projects
    utilizar .ancestor(3) para retornar a la raíz
"""

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    BASE_DIR.child('templates'),
)

STATICFILES_DIRS = (
    BASE_DIR.child('static'),
)

MEDIA_ROOT = '' #BASE_DIR.child('media')
MEDIA_URL = ''

#==>>> server ftp images <<<==#
#In models.py you can write:
# from FTPStorage import FTPStorage
# fs = FTPStorage()
# class FTPTest(models.Model):
#     file = models.FileField(upload_to='a/b/c/', storage=fs)

#FTP_STORAGE_LOCATION = '[a]ftp://<user>:<pass>@<host>:<port>/[path]'
FTP_STORAGE_LOCATION = 'ftp://encoding:encid2015@ftp.encodingideas.heliohost.org:21/evento/'


#MEDIA_URL = 'ftp://encoding:encid2015@ftp.encodingideas.heliohost.org/evento/'