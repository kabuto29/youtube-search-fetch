import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management import BaseCommand
 
class Command(BaseCommand):
    """Django command to pause execution until db is available"""
 
    def handle(self, *args, **options):
        self.stdout.write('Waiting for database... waiting for 10 sec')
        time.sleep(10)
        db_conn = None
        while db_conn == None:
            self.stdout.write('in while')
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable, waititng 1 second...')
                time.sleep(1)
 
        self.stdout.write(self.style.SUCCESS('Database available!'))