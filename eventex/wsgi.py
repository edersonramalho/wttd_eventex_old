"""
WSGI config for eventex project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
from dj_static import Cling ## para controle dos statics, é uma app wsgi
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eventex.settings")

application = Cling(get_wsgi_application())# só add Cling 
"""
O cling vai processar antes de qualquer requisição
e tratar os statics vindos de host atual e/ou outros(Amazom, etc)
"""
