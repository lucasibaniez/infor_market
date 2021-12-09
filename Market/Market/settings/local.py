from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "infor_market",
        "USER": "postgres",
        "PASSWORD": "a",
        "HOST": "localhost",
        "PORT": "5432"
    }
}
