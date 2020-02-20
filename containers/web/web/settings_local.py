from .settings_base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'elabel',
        'USER': 'tvi',
        'PASSWORD': 'ZachAttack!',
        'HOST': '127.19.0.2',
        'PORT': os.getenv('POSTGRES_SERVICE_PORT', 5432)
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_ROOT = '/tmp/elables/static'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
#    '/var/www/static/',
]
DEBUG = True
# This should not be done in production, but okay for now.
ALLOWED_HOSTS = ['*']