import datetime
from django.test import TestCase
from .models import Meetup


EVENT_JSON = """
{
  "results": [
    {
      "venue": {
        "id": 1,
        "lon": 0,
        "name": "Test Location",
        "state": "MO",
        "address_1": "1 First Street",
        "lat": 0,
        "city": "Saint Louis",
        "country": "us"
      },
      "id": "tested",
      "utc_offset": -18000000,
      "time": 1394667000000,
      "waitlist_count": 0,
      "updated": 1390257618000,
      "yes_rsvp_count": 5,
      "created": 1389298531000,
      "event_url": "http:\/\/testurl",
      "description": "<p>Description<\/p>",
      "how_to_find_us": "We're in a cave",
      "name": "Event Name",
      "headcount": 0,
      "group": {
        "id": 1,
        "group_lat": 0,
        "name": "Meetup Name",
        "group_lon": 0,
        "join_mode": "open",
        "urlname": "Meetup-Name",
        "who": "Folks"
      }
    }
  ]
}
"""

class MeetupsViewTest(TestCase):
    def test_groups_view_sanity(self):
        response = self.client.get('/groups/meetups/')
        self.assertEqual(response.status_code, 200)
    
    def test_groups_view_contains_meetups(self):
        response = self.client.get('/groups/meetups/')
        self.assertContains(response, 'Meetups')
    
    def test_groups_view_contains_stl_python(self):
        Meetup.objects.create(name='Test Meetup')
        response = self.client.get('/groups/meetups/')
        self.assertContains(response, 'Test Meetup')
    
    def test_meetup_next_event(self):
        meetup = Meetup(next_event_json=EVENT_JSON)
        event = meetup.get_next_event()
        
        self.assertEqual(event['name'], 'Event Name')
    
    def test_meetup_next_event_venue(self):
        meetup = Meetup(next_event_json=EVENT_JSON)
        event = meetup.get_next_event()
        venue = event['venue']
        
        self.assertEqual(venue['name'], 'Test Location')
    
    def test_meetup_next_event_group(self):
        meetup = Meetup(next_event_json=EVENT_JSON)
        event = meetup.get_next_event()
        group = event['group']
        
        self.assertEqual(group['name'], 'Meetup Name')
    
    def test_meetup_next_event_datetime(self):
        meetup = Meetup(next_event_json=EVENT_JSON)
        event_date = meetup.get_next_event_time()
        
        self.assertEqual(event_date, datetime.datetime(2014, 03, 12, 18, 30))
