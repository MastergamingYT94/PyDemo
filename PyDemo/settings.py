"""
Django settings for PyDemo project.

<<<<<<< HEAD
Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
=======
Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
from pathlib import Path
import os
import dj_database_url
>>>>>>> 8bd5679f0915566d6e588b99e4c05e916e2e99f6
import cloudinary

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
<<<<<<< HEAD
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-x2s7sdu)nsk=9xab9t2ylho5%n%0nvbme8p=2&dl!6$3ny!&mh'
=======
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xdiw%jm!3b12hck0cewbu*vh+3)nibz%v3i^$*d^j4d_#m!ght'
>>>>>>> 8bd5679f0915566d6e588b99e4c05e916e2e99f6

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['http://localhost:4200',
<<<<<<< HEAD
                 '127.0.0.1', 'pycommerceapp.herokuapp.com', 'https://angularpycommerce.herokuapp.com']
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost:4200',
    'https://angularpycommerce.herokuapp.com'
=======
                 '127.0.0.1', 'pycommerceapp.herokuapp.com', 'http://angularpycommerce.herokuapp.com']
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost:4200',
    'http://angularpycommerce.herokuapp.com'

>>>>>>> 8bd5679f0915566d6e588b99e4c05e916e2e99f6
)

OPTIONS = {
    'timeout': 20,
}

<<<<<<< HEAD
SITE_ID = 1
# SITE_URL = "http://127.0.0.1:8000"
SITE_URL = "http://pycommerceapp.herokuapp.com"
=======
>>>>>>> 8bd5679f0915566d6e588b99e4c05e916e2e99f6
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
<<<<<<< HEAD
    'django.contrib.messages',
    'django.contrib.staticfiles',
=======
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
>>>>>>> 8bd5679f0915566d6e588b99e4c05e916e2e99f6
    'PyCommerce.apps.PycommerceConfig',
    'api.apps.ApiConfig',
    'rest_framework',
    'corsheaders',
    'cloudinary'
]
<<<<<<< HEAD

=======
SITE_ID = 1
# SITE_URL = "http://127.0.0.1:8000"
SITE_URL = "http://pycommerceapp.herokuapp.com"
>>>>>>> 8bd5679f0915566d6e588b99e4c05e916e2e99f6
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'PyDemo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
<<<<<<< HEAD
        'DIRS': [],
=======
        'DIRS': [os.path.join(BASE_DIR, 'PyCommerce/templates')],
>>>>>>> 8bd5679f0915566d6e588b99e4c05e916e2e99f6
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

WSGI_APPLICATION = 'PyDemo.wsgi.application'


# Database
<<<<<<< HEAD
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
=======
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
>>>>>>> 8bd5679f0915566d6e588b99e4c05e916e2e99f6

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
<<<<<<< HEAD


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
=======
# DATABASES['default'].update(dj_database_url.config())

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
DATE_INPUT_FORMATS = ['%d/%m/%Y']
DATE_FORMAT = r'd/m/Y'
# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
>>>>>>> 8bd5679f0915566d6e588b99e4c05e916e2e99f6

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
<<<<<<< HEAD
# https://docs.djangoproject.com/en/3.2/topics/i18n/
=======
# https://docs.djangoproject.com/en/3.1/topics/i18n/
>>>>>>> 8bd5679f0915566d6e588b99e4c05e916e2e99f6

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
<<<<<<< HEAD
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
=======
# https://docs.djangoproject.com/en/3.1/howto/static-files/
>>>>>>> 8bd5679f0915566d6e588b99e4c05e916e2e99f6

STATIC_ROOT = os.path.join(BASE_DIR, "PyCommerce/")
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "PyCommerce/static"),
)

<<<<<<< HEAD
=======
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/images/')
MEDIA_URL = '/media/images/'

>>>>>>> 8bd5679f0915566d6e588b99e4c05e916e2e99f6
cloudinary.config(
    cloud_name="pycommerce",
    api_key="544135185544278",
    api_secret="V_TChoN8UXBeZ7lS58cZDYxAjWI",
    secure=True
)
