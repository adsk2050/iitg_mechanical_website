from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['mechweb2.centralindia.cloudapp.azure.com', '52.172.166.108', '127.0.0.1', '0.0.0.0']

INTERNAL_IPS = ("127.0.0.1, 0.0.0.0")

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = INSTALLED_APPS + [
	'debug_toolbar',
    'sslserver',
]

MIDDLEWARE = MIDDLEWARE+[
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

try:
    from .local import *
except ImportError:
    pass

BASE_URL = 'https://mechweb2.centralindia.cloudapp.azure.com/mech/'
