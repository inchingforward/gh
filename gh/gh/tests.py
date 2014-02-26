from django.test import LiveServerTestCase
from django.test import TestCase
from django.contrib.auth.models import User
from selenium import webdriver
import views
from .models import Post

class HomePageTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        self.browser.get(self.live_server_url)
        self.user = User.objects.create(username='test')
    
    def tearDown(self):
        self.browser.quit()
    
    def test_home_page_sanity_check(self):
        self.assertEqual("Gateway Hackers", self.browser.title)
    
    def test_home_page_has_no_posts(self):
        posts = self.browser.find_elements_by_css_selector('#post-list li')
        self.assertEqual(len(posts), 0)

    def test_home_page_has_anonymous_user_links(self):
        self.assertGreaterEqual(len(self.browser.find_elements_by_link_text('Log in')), 1)
        self.assertGreaterEqual(len(self.browser.find_elements_by_link_text('Sign up')), 1)
        self.assertGreaterEqual(len(self.browser.find_elements_by_link_text('About')), 1)
    
    def test_home_page_with_posts(self):
        for x in range(30):
            item = Post()
            item.title = 'Title %s' % x
            item.visible = True
            item.user = self.user
            item.save()
        
        self.browser.get(self.live_server_url)
        self.assertEqual(len(self.browser.find_elements_by_css_selector('#post-list li')), views.PAGINATE_BY)