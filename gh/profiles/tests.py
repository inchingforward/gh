from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile


class ProfileTest(TestCase):
    def test_uses_first_name_for_short_name(self):
        user = User(username='testing', first_name='Atticus', last_name='Finch')
        profile = Profile(user=user)
        
        self.assertEqual('Atticus', profile.get_short_name())
    
    def test_uses_username_when_missing_name(self):
        user = User(username='testing')
        profile = Profile(user=user)
        
        self.assertEqual('testing', profile.get_short_name())
    
    def test_full_name_no_name(self):
        user = User(username='testing')
        profile = Profile(user=user)
        
        self.assertEqual('testing', profile.get_full_name())
    
    def test_full_name_only_has_first_name(self):
        user = User(username='testing', first_name='Atticus')
        profile = Profile(user=user)
        
        self.assertEqual('Atticus', profile.get_full_name())
    
    def test_full_name_has_first_and_last(self):
        user = User(username='testing', first_name='Atticus', last_name='Finch')
        profile = Profile(user=user)
        
        self.assertEqual('Atticus Finch', profile.get_full_name())
    
    def test_has_projects_no_projects(self):
        profile = Profile()
        
        self.assertFalse(profile.has_projects())
    
    def test_has_project_with_projects(self):
        profile = Profile(project_1_url='http://gatewayhackers.com')
        
        self.assertTrue(profile.has_projects())
    
    def test_has_elsewhere_no_elsewheres(self):
        profile = Profile()
        
        self.assertFalse(profile.has_elsewhere())
    
    def test_has_elswhere_with_elsewhere(self):
        profile = Profile(elsewhere_1_url='http://gatewayhackers.com')
        
        self.assertTrue(profile.has_elsewhere())

