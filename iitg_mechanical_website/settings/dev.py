try:
    from .base import *
except ImportError:
    pass

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

INTERNAL_IPS = ("172.16.72.79, 127.0.0.1, 0.0.0.0")

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = INSTALLED_APPS + [
	# 'debug_toolbar',
    'sslserver',
]

MIDDLEWARE = MIDDLEWARE+[
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# BASE_URL = 'https://mechweb2.centralindia.cloudapp.azure.com/mech/'
