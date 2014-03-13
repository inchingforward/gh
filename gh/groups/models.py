import datetime
import json
from django.db import models


class Meetup(models.Model):
    name = models.TextField()
    url = models.URLField()
    group_urlname = models.TextField()
    details = models.TextField(blank=True)
    next_event_json = models.TextField(blank=True)
    next_event_updated_date = models.DateTimeField(null=True)
    
    def get_next_event(self):
        if self.next_event_json:
            try:
                return json.loads(self.next_event_json)['results'][0]
            except:
                pass
        
        return {}
    
    def get_next_event_time(self):
        millis = self.get_next_event()['time']
        
        if millis:
            return datetime.datetime.fromtimestamp(millis/1000.0)
        
        return None
    
    class Meta:
        ordering = ['name']
    
    def __unicode__(self):
        return self.name

