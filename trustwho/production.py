from trustwho.settings import *

DEBUG = True
MEDIA_URL = '/media/'
MEDIA_ROOT = "/home/likun/data/media/"

STATIC_ROOT = '/home/likun/data/static/'

STATICFILES_DIRS = STATICFILES_DIRS + (
    '/home/likun/env/lib/python2.7/site-packages/django/contrib/admin/static/',
)
