from .settings_base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': os.getenv('VEAT_DB_SERVICE_HOST', 'db'), # Use k8s env var otherwise use docker container name.
        'PORT': os.environ['DB_PORT']
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_ROOT = '/static' #todo: This should probably be somewhere else like /var/www/static
STATIC_URL = 'http://storage.googleapis.com/vessel-energy/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
#    '/var/www/static/',
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/veat/debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
ALLOWED_HOSTS = ['web', 'localhost']