from six import string_types
from django.conf import settings
from django.core.management.base import BaseCommand

from ...server import shell


class Command(BaseCommand):
    help = 'Runs each livereload task once.'

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)

    def handle(self, *args, **options):
        for task in getattr(settings, 'LIVERELOAD_TASKS', []):
            func = task.get('task')
            print('Run: ', func)
            if isinstance(func, string_types):
                func = shell(func)
            func()
