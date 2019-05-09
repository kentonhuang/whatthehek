# Production is what the live code (customer facing) uses
from example.settings.base import *


# Debug option
# https://docs.djangoproject.com/en/2.0/ref/settings/#debug
# Ensure debug is always false in production environment
DEBUG = False


# Databases
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
# Production environment should use the intended target production database
# such as MySQL, Postgres, MongoDB etc
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    },
}