"""
Django settings for final project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
SITE_ROOT=os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p8(wfpcco44*ovg5w@z@e&$b()hm(l-))&^!k=wrsph%efv4+s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'final.urls'

WSGI_APPLICATION = 'final.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'final',
        'USER': 'root',
        'PASSWORD': 'scut8711',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {"init_command": "SET storage_engine=INNODB"},
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/templates-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(SITE_ROOT, 'static')

UPLOAD_PATH = os.path.join(STATIC_ROOT, 'Upload')

STATICFILES_DIRS = (
    ("Upload", os.path.join(STATIC_ROOT,'Upload')),
    ("Photo", os.path.join(UPLOAD_PATH,'Photo')),
    ("Head", os.path.join(UPLOAD_PATH,'Head')),
)
