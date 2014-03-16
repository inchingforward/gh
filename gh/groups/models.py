import datetime
import json
from django.db import models


class Meetup(models.Model):
    name = models.TextField()
    url = models.URLField()
    group_urlname = models.TextField()
    details = models.TextField(blank=True)
    next_event_json = models.TextField(blank=True)
    next_event_updated_date = models.DateTimeField(blank=True, null=True)
        
    def get_next_event(self):
        events = self.meetupevent_set.all()
        if events:
            return self.meetupevent_set.all()[0]
        return None
    
    class Meta:
        ordering = ['name']
    
    def __unicode__(self):
        return self.name

class MeetupEvent(models.Model):
    meetup = models.ForeignKey(Meetup)
    name = models.TextField()
    venue_name = models.TextField(blank=True)
    address_1 = models.TextField(blank=True)
    address_2 = models.TextField(blank=True)
    address_3 = models.TextField(blank=True)
    city = models.TextField(blank=True)
    state = models.TextField(blank=True)
    zip_code = models.TextField(blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    event_date = models.DateTimeField()
    modified = models.DateTimeField(auto_now=True)
    url = models.URLField(blank=True)
    
    def __unicode__(self):
        return self.name

