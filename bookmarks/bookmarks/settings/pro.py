from .base import *

DEBUG = False

ADMINS = (
    ('admin', 'email@mydomain.com'),
)

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True

ROOT_URLCONF = 'bookmarks.urls'

ALLOWED_HOSTS = ['bookmarks.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bookmarks',
        'USER': 'bookmarks',
        'PASSWORD': '456',
    }
}
