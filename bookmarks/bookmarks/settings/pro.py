from .base import *

DEBUG = False

ADMINS = (
    config('ADMIN_NAME', 'ADMIN_EMAIL'),
)

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True

ROOT_URLCONF = 'bookmarks.urls'

ALLOWED_HOSTS = ['bookmarks.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DATABASES_NAME'),
        'USER': config('DATABASES_USER'),
        'PASSWORD': config('DATABASES_PASSWORD'),
    }
}

