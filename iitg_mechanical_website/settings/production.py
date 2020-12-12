try:
    from .base import *
except ImportError:
    pass

DEBUG = True

ALLOWED_HOSTS = ['intranet.iitg.ac.in/mech', '172.16.72.79']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash

SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE =True
CSRF_COOKIE_SECURE=True
CSRF_TRUSTED_ORIGINS = ['intranet.iitg.ac.in']

FIRST_DAY_OF_WEEK = 1

# SESSION_COOKIE_DOMAIN=None
SOCIAL_AUTH_STRATEGY = 'iitg_mechanical_website.strategy.CustomDjangoStrategy'
SESSION_COOKIE_SAMESITE = None
SESSION_COOKIE_SECURE=False
