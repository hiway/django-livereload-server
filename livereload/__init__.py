"""django-livereload"""
__version__ = '0.2.3'
__license__ = 'BSD License'

__author__ = 'Tomas Walch'
__email__ = 'tomaswalch@gmail.com'

__url__ = 'https://github.com/tjwalch/django-livereload-server'


def livereload_port():
    from django.conf import settings
    return int(getattr(settings, 'LIVERELOAD_PORT', 35729))


def livereload_host():
    from django.conf import settings
    return getattr(settings, 'LIVERELOAD_HOST', '127.0.0.1')


def livereload_proxy_port():
    from django.conf import settings
    return int(getattr(settings, 'LIVERELOAD_PROXY_PORT', None))


def livereload_proxy_host():
    from django.conf import settings
    return getattr(settings, 'LIVERELOAD_PROXY_HOST', None)


def livereload_proxy_secure():
    from django.conf import settings
    return getattr(settings, 'LIVERELOAD_PROXY_SECURE', False) is True
