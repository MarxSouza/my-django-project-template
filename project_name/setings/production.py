from .settings import *

INSTALLED_APPS += ('compressor',)
ALLOWED_HOSTS += ['127.0.0.1']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}