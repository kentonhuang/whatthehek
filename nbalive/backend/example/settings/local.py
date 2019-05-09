# For local development purposes.
from example.settings.base import *


# Debug option
# https://docs.djangoproject.com/en/2.0/ref/settings/#debug
# Local can leave debug enabled
DEBUG = True


# Databases
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
# Using SQLite by default on local development environment
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}