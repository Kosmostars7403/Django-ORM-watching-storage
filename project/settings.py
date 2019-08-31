import os
from environs import Env

env = Env()
env.read_env()

SECRET_KEY = env.str("SECRET_KEY")

DATABASES = {
    'default': {
        'ENGINE': env.str("DB_ENGINE"),
        'HOST': env.str("DB_HOST"),
        'PORT': env.str("DB_PORT"),
        'NAME': env.str("DB_NAME"),
        'USER': env.str("DB_USER"),
        'PASSWORD': env.str("DB_PASSWORD"),
    }
}

DEBUG = env.bool("DEBUG")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = ['datacenter']

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]

