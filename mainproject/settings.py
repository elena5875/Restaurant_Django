#settings.py
from pathlib import Path  # Add this import
import os
import sys  # Add this import
import dj_database_url
from dotenv import load_dotenv
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Load environment variables from .env if it exists
load_dotenv()

# Print DATABASE_URL to debug
print("DATABASE_URL:", os.environ.get("DATABASE_URL"))

# Build paths inside the project like this: BASE_DIR / 'subdir'
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", '(buk#6n2v%(rh_#nouc79jlt*4lbk-nh=(c_5^ihx+lggn8akt')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'djagnoresto-267ab1695d73.herokuapp.com',
    '8000-elena5875-restaurantdja-y713ht9ewxi.ws.codeinstitute-ide.net'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'restaurant',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'mainproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'mainproject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configure Cloudinary
cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME', 'dh5i9qtjf'),
    api_key=os.environ.get('CLOUDINARY_API_KEY', '771193164774472'),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET', '7ekPLUqJq0Od4eD2zBi5gufWl7w')
)

# CSRF Trusted Origins
CSRF_TRUSTED_ORIGINS = os.environ.get('CSRF_TRUSTED_ORIGINS', '').split(',')

# Code Institute Workspace URL
CODEINSTITUTE_WORKSPACE_URL = 'https://8000-elena5875-restaurantdja-y713ht9ewxi.ws.codeinstitute-ide.net'

# Add Code Institute workspace URL to CSRF trusted origins
CSRF_TRUSTED_ORIGINS.append(CODEINSTITUTE_WORKSPACE_URL)

# Add wildcard for Code Institute subdomains
CSRF_TRUSTED_ORIGINS += ['https://*.codeinstitute-ide.net']

# Ensure Heroku URL is also included
CSRF_TRUSTED_ORIGINS.append('https://djagnoresto-267ab1695d73.herokuapp.com')



# Email settings
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'theforkrestaurant@yahoo.com')
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend')
ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', 'theforkrestaurant@gmail.com')