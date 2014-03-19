import datetime
import json
import requests
import sys
import time
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from groups.models import Meetup, MeetupEvent


EVENTS_URL = 'http://api.meetup.com/2/events?&group_urlname=%s&page=1&sign=true&key=%s'

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not settings.MEETUP_API_KEY:
            raise CommandError('Missing GH_MEETUP_API_KEY environment variable')
        
        meetups = Meetup.objects.all()
        
        if not meetups:
            raise CommandError("No meetups found")
        
        self.stdout.write('Updating %s meetups...' % len(meetups))
        
        events = MeetupEvent.objects.all()
        events.delete()
        
        meetups = Meetup.objects.all()
        
        for meetup in meetups:
            self.stdout.write("Updating %s..." % meetup.name)
            
            res = requests.get(EVENTS_URL % (meetup.group_urlname, settings.MEETUP_API_KEY))
            
            if res and res.text:
                try:
                    event = json.loads(res.text)['results'][0]
                    venue = event['venue']
                    
                    me = MeetupEvent()
                    me.meetup = meetup
                    me.name = event['name']
                    me.venue_name = venue['name']
                    me.address_1 = venue.get('address_1', '')
                    me.address_2 = venue.get('address_2', '')
                    me.address_3 = venue.get('address_3', '')
                    me.city = venue.get('city', '')
                    me.state = venue.get('state', '')
                    me.zip_code = venue.get('zip', '')
                    me.latitude = venue['lat']
                    me.longitude = venue['lon']
                    me.event_date = datetime.datetime.fromtimestamp(event['time']/1000.0)
                    me.url = event['event_url']
                    me.save()
                    
                    self.stdout.write("  OK")
                except:
                    self.stderr.write("Unexpected error:", sys.exc_info()[0])
            
            time.sleep(1)
