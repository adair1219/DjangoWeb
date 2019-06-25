
"""
导入所有的 基础设置
"""
from .base import *  # NOQA

DEBUG = True

"""
设置开发环境的 数据库
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}