import os

from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wu_tm&unmshc^nxgo*^u!wvi!gkz9h+x+-2ahtqs#2!bkk-r*y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'PORT': 3306,
        'NAME': 'mail_list',
        'USER': 'root',
        'PASSWORD':	'happy=2016',
        'DEFAULT-CHARACTER-SET': 'utf8',
    },
}
		


INTERNAL_IPS = ['192.168.56.1']

INSTALLED_APPS += (
    'autofixture',
)

STATICFILES_DIRS.append(
    os.path.join(BASE_DIR, os.pardir, 'frontend', 'build'),
)
