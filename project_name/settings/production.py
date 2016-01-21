from .base import *

INSTALLED_APPS += ['compressor']

ALLOWED_HOSTS += ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '{{ project_name }}',
        'USER':'', 'PASS':'',
        'HOST':'', 'PORT':'3306',
    }
}