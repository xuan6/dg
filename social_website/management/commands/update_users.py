from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.db import models
from tastypie.models import create_api_key

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-a', '--all',
                    action='store_true',
                    default=False,
                    help='Update users with api keys'),
        )

    def handle(self, *args, **options):
        if (options['all']):
            self.update_users()
    
    def update_users(self):
        try:
            models.signals.post_save.connect(create_api_key,sender=User)
        except Exception as e:
             print "error in updating users"
             print e