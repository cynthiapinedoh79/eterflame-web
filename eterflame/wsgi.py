"""
WSGI config for eterflame project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise  # <-- 1. Import Whitenoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eterflame.settings")

# 2. Get the default application first
application = get_wsgi_application()

# 3. Wrap the default application with Whitenoise
application = WhiteNoise(application)
