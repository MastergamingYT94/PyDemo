"""
ASGI config for PyDemo project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
=======
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
>>>>>>> 8bd5679f0915566d6e588b99e4c05e916e2e99f6
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PyDemo.settings')

application = get_asgi_application()
