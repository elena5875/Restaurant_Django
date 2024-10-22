from pathlib import Path  # Import for handling filesystem paths
import os  # Import for interacting with the operating system
import sys  # Import for accessing command-line arguments
import dj_database_url  # Library to parse database URLs
from dotenv import load_dotenv  # Library to load environment variables from a .env file
import cloudinary  # Library for managing images with Cloudinary
import cloudinary.uploader
import cloudinary.api

# Load environment variables from .env if it exists
load_dotenv()

# Debugging: Print DATABASE_URL to ensure it's being loaded correctly
print("DATABASE_URL:", os.environ.get("DATABASE_URL"))

# Build paths inside the project like this: BASE_DIR / 'subdir'
BASE_DIR = Path(__file__).resolve().parent.parent  # Define the base directory for the project

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", '(buk#6n2v%(rh_#nouc79jlt*4lbk-nh=(c_5^ihx+lggn8akt')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", "False") == "True"  # Set debug mode based on environment variable

# List of allowed hosts for the application
ALLOWED_HOSTS = [
    'localhost',  # Allow local development
    '127.0.0.1',  # Allow local development
    'djagnoresto-267ab1695d73.herokuapp.com',  # Heroku production URL
    '8000-elena5875-restaurantdja-y713ht9ewxi.ws.codeinstitute-ide.net'  # Code Institute IDE URL
    '8001-elena5875-restaurantdja-y713ht9ewxi.ws.codeinstitute-ide.net'
    '*'
]

ALLOWED_HOSTS.append('8000-elena5875-restaurantdja-y713ht9ewxi.ws.codeinstitute-ide.net')


# Custom error handler for 404 errors
handler404 = 'mainproject.views.custom_404'

# Application definition

# List of installed apps for the Django project
INSTALLED_APPS = [
    'django.contrib.admin',  # Django admin interface
    'django.contrib.auth',  # Authentication system
    'django.contrib.contenttypes',  # Content types framework
    'django.contrib.sessions',  # Session framework
    'django.contrib.messages',  # Messaging framework
    'django.contrib.staticfiles',  # Static file management
    'restaurant',  # Custom restaurant app
]

# Middleware configuration for request processing
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Security middleware
    'django.contrib.sessions.middleware.SessionMiddleware',  # Session handling middleware
    'django.middleware.common.CommonMiddleware',  # Common middleware
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF protection middleware
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Authentication middleware
    'django.contrib.messages.middleware.MessageMiddleware',  # Message handling middleware
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Clickjacking protection
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Middleware for serving static files efficiently
]

# URL configuration for the project
ROOT_URLCONF = 'mainproject.urls'

# Template settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Template engine
        'DIRS': [BASE_DIR / 'templates'],  # Directories to look for templates
        'APP_DIRS': True,  # Automatically search in app directories
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Debug context processor
                'django.template.context_processors.request',  # Request context processor
                'django.contrib.auth.context_processors.auth',  # Auth context processor
                'django.contrib.messages.context_processors.messages',  # Messages context processor
            ],
        },
    },
]

# WSGI application configuration
WSGI_APPLICATION = 'mainproject.wsgi.application'

# Database configuration
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if 'test' in sys.argv:  # Use SQLite for testing
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',  # SQLite backend
            'NAME': BASE_DIR / 'db.sqlite3',  # Database file path
        }
    }
else:  # Use the database specified in the DATABASE_URL environment variable
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))  # Parse database URL
    }

# Password validation settings
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # User attribute similarity validator
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Minimum length validator
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Common password validator
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Numeric password validator
    },
]

# Internationalization settings
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'  # Default language code

TIME_ZONE = 'UTC'  # Default time zone

USE_I18N = True  # Enable internationalization

USE_TZ = True  # Enable time zone support

# Static files configuration
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'  # URL to access static files

STATIC_ROOT = BASE_DIR / 'staticfiles'  # Directory to collect static files

STATICFILES_DIRS = [
    BASE_DIR / 'static',  # Ensure this directory contains 'css/media_queries.css'
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  # Storage backend for static files

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Default field type for primary keys

# Configure Cloudinary for media uploads
cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME', 'dh5i9qtjf'),  # Cloudinary cloud name
    api_key=os.environ.get('CLOUDINARY_API_KEY', '771193164774472'),  # Cloudinary API key
    api_secret=os.environ.get('CLOUDINARY_API_SECRET', '7ekPLUqJq0Od4eD2zBi5gufWl7w')  # Cloudinary API secret
)

# CSRF Trusted Origins configuration
CSRF_TRUSTED_ORIGINS = os.environ.get('CSRF_TRUSTED_ORIGINS', '').split(',')  # Load trusted origins from environment variable

# Code Institute Workspace URL
CODEINSTITUTE_WORKSPACE_URL = 'https://8000-elena5875-restaurantdja-y713ht9ewxi.ws.codeinstitute-ide.net'

# Add Code Institute workspace URL to CSRF trusted origins
CSRF_TRUSTED_ORIGINS.append(CODEINSTITUTE_WORKSPACE_URL)

# Add wildcard for Code Institute subdomains
CSRF_TRUSTED_ORIGINS += ['https://*.codeinstitute-ide.net']  # Allow all subdomains of Code Institute

# Ensure Heroku URL is also included in trusted origins
CSRF_TRUSTED_ORIGINS.append('https://djagnoresto-267ab1695d73.herokuapp.com')  # Heroku production URL

# Email settings
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'theforkrestaurant@yahoo.com')  # Default email address for sending emails
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend')  # Email backend configuration
ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', 'theforkrestaurant@gmail.com')  # Email address for admin notifications
