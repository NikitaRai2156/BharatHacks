# *-* coding: utf-8 -*-

from .common import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bharathacks',
        'USER': 'root',
        'PASSWORD': '',
    }
}
