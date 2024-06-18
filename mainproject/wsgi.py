"""
WSGI config for mainproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""
#wsgi.py
import os
import dotenv
from django.core.wsgi import get_wsgi_application

# Load environment variables from .env file
dotenv.load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mainproject.settings')

application = get_wsgi_application()
