"""
ASGI config for JobBoard_Project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JobBoard_Project.settings')
django.setup()

from django.core.asgi import get_asgi_application


application = get_asgi_application()
