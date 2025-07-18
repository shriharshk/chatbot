"""WSGI config for chatbot project."""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatbot_project.settings')
application = get_wsgi_application()
