from .settings import *

INSTALLED_APPS += ('compressor',)
ALLOWED_HOSTS += ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '{{ project_name }}',
        'USER':'', 'PASS':'',
        'HOST':'', 'PORT':'3306',
    }
}