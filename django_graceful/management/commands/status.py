from django_graceful import Graceful
from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):
    help = "TODO"
    
    def handle_noargs(self, **options):
        for b in Graceful().backends:
            print b

