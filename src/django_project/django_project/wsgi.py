"""
WSGI config for django_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# fixed param: PROJECT_PROFILE --指所有 django_project 下的文件
# param: profile --profile = 'develop.py'
# targe： 随意转换 开发环境与生产环境
profile = os.environ.setdefault('DJANGO_PROJECT_PROFILE', 'develop')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings.%s' % profile)

application = get_wsgi_application()
