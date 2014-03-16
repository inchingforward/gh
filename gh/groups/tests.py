import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Meetup, MeetupEvent


class MeetupsViewTest(TestCase):
    def test_meetups_view_sanity(self):
        response = self.client.get('/groups/meetups/')
        self.assertEqual(response.status_code, 200)
    
    def test_meetups_view_contains_meetups(self):
        response = self.client.get('/groups/meetups/')
        self.assertContains(response, 'Meetups')
    
    def test_meetups_view_contains_test_meetup(self):
        meetup = Meetup.objects.create(name='Test Meetup')
        MeetupEvent.objects.create(name='Test Event', meetup=meetup, latitude=0.0, longitude=0.0, event_date=timezone.now())
        response = self.client.get('/groups/meetups/')
        self.assertContains(response, 'Test Event')
    
    def test_meetups_view_meetup_returns_next_event(self):
        meetup = Meetup.objects.create(name='Test Meetup')
        MeetupEvent.objects.create(name='Test Event', meetup=meetup, latitude=0.0, longitude=0.0, event_date=timezone.now())
        self.assertEqual('Test Event', meetup.get_next_event().name)
