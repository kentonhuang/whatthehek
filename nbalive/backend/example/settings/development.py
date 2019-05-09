# Development environment mimics production for development purposes.
from example.settings.base import *


# Debug option
# https://docs.djangoproject.com/en/2.0/ref/settings/#debug
# Development can leave debug enabled
DEBUG = True


# Databases
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
# Development environment should use the intended target production database
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