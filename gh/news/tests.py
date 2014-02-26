from django.test import TestCase
from django.contrib.auth.models import User
from .models import NewsItem


class NewsItemListTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testing')
        
    def test_news_list_displays(self):
        NewsItem.objects.create(title='Test title', details='Test details', user=self.user)
        
        response = self.client.get('/news/')
        
        self.assertContains(response, 'Test title')
        self.assertContains(response, 'Test details')
