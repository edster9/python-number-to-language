"""
WSGI config for number_to_language project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# read the ENV variable from shell
environment = os.environ.get('ENV', 'local')

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      f'number_to_language.settings.{environment}')

application = get_wsgi_application()
