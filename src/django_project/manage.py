#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    # fixed param: DJANGO_PROJECT_PROFILE --指所有 django_project 下的文件
    # param: profile --profile = 'develop.py'
    # targe： 随意转换 开发环境与生产环境
    profile = os.environ.get('DJANGO_PROJECT_PROFILE', 'develop')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings.%s' % profile)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
