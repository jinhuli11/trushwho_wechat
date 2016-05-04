# coding: utf-8
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
from django.utils.translation import gettext_lazy as _
"""
Django settings for trustwho project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import sys 
reload(sys)
sys.setdefaultencoding('utf-8')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_abs(path):
    return os.path.join(BASE_DIR, path)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5o6bn-lljhwz#m6od%8y5ipq#@wi_7_81165j0*-kzbd85@(oa'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
#     'django_admin_bootstrapped',
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'common',
    'bigvs',
    'articles',
    'wechat',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'trustwho.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            get_abs('templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

WSGI_APPLICATION = 'trustwho.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wealth_db',
        'HOST': 'rdsw5ilfm0dpf8lee609.mysql.rds.aliyuncs.com',
        'PORT': 3306,
        'USER': 'licj',
        'PASSWORD': 'AAaa_0504'
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'django_cache_table',
    }
}

# CACHES = {
#     'default': {
#         'BACKEND': 'redis_cache.cache.RedisCache',
#         'LOCATION': '123.56.233.112:6379',
#         "OPTIONS": {
#             'DB': 1,
#             'PASSWORD': 'redis7890',
#             "CLIENT_CLASS": "redis_cache.client.DefaultClient",
#         },
#     },
# }
# REDIS_TIMEOUT = 7 * 24 * 60 * 60
# CUBES_REDIS_TIMEOUT = 60 * 60
# NEVER_REDIS_TIMEOUT = 365 * 24 * 60 * 60

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh_CN'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    get_abs('static'),
)

# django_sult config
SUIT_CONFIG = {
    'ADMIN_NAME': '信谁微信后台管理',
    
    'MENU_ICONS': {
        'sites': 'icon-leaf',
    },
        
    'MENU': (
        'sites',
        # Rename app and set icon
        {'app': 'wechat', 'label': _(u'微信用户管理'), 'icon':'icon-user'},
        {'app': 'bigvs', 'label': _(u'大V管理'), 'icon':'icon-heart'},
        {'app': 'articles', 'label': _(u'文章管理'), 'icon':'icon-list-alt'},
        {'label': _(u'系统用户设置'), 'icon': 'icon-cog', 'models': ('auth.user', 'auth.group')},
    )
    
    
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': get_abs('debug.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'debug': {
            'handlers': ['file'],
            'level': 'INFO',
        }
    }
}

# 微信公众号配置
WECHAT_APPID = 'wx9eba0081228e07ec'
WECHAT_APPSECRET = 'ac665808a72856f499e11c37a293dce0'
WECHAT_TOKEN = 'B0quTechWebchat'
