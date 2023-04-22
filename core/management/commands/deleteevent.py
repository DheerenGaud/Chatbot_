from django.core.management.base import BaseCommand
from django.utils import timezone
from chatbot.models import Newevent
from datetime import timedelta






class Command(BaseCommand):
    help = 'Deletes expired events.'

    def handle(self, *args, **options):
        now = timezone.now()
        print(now)
        
        expired_events = Newevent.objects.filter(eventend__lt=now)
        expired_events.delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted expired events.'))
        
        
        
        
# from django.core.management.base import BaseCommand
# from django.utils import timezone


# class Command(BaseCommand):
#     help = 'Deletes data older than 30 days'

#     def handle(self, *args, **options):
#        print("hellow 2")
#        now = timezone.now()
#        expired_events = Newevent.objects.filter(eventend__lt=now)
#        expired_events.delete()



      