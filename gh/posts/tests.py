from django.test import LiveServerTestCase
from django.test import TestCase
from selenium import webdriver
import views


# Functional Tests
class HomePageTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        self.browser.get(self.live_server_url)
    
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
