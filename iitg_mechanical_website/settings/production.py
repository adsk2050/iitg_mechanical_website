try:
    from .base import *
except ImportError:
    pass

DEBUG = True

ALLOWED_HOSTS = ['172.16.72.79']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash

SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE =True
CSRF_COOKIE_SECURE=True

FIRST_DAY_OF_WEEK = 1
