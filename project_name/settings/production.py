from .base import *

DEBUG = False

ALLOWED_HOSTS = ['{{ project_name }}.com.br']

INSTALLED_APPS += ['compressor',]

DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '{{ project_name }}',   
        'USER': '{{ project_name }}', 
        'PASS': '', 
        'HOST': '', 
    },
}
