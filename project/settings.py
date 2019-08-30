from dotenv import load_dotenv
import os
from dotenv.main import dotenv_values


load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

DATABASES = {
    'default': {
        'ENGINE': os.getenv("DB_ENGINE"),
        'HOST': os.getenv("DB_HOST"),
        'PORT': os.getenv("DB_PORT"),
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
    }
}

DEBUG = os.getenv("DEBUG")

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

