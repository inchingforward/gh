from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile


class ProfileModelTest(TestCase):
    def test_short_name_uses_first_name_when_present(self):
        user = User(username='testing', first_name='Atticus', last_name='Finch')
        profile = Profile(user=user)
        
        self.assertEqual('Atticus', profile.get_short_name())
    
    def test_short_name_uses_username_when_missing_first_name(self):
        user = User(username='testing')
        profile = Profile(user=user)
        
        self.assertEqual('testing', profile.get_short_name())
    
    def test_full_name_uses_username_when_missing_first_and_last_name(self):
        user = User(username='testing')
        profile = Profile(user=user)
        
        self.assertEqual('testing', profile.get_full_name())
    
    def test_full_name_uses_first_name_when_missing_last_name(self):
        user = User(username='testing', first_name='Atticus')
        profile = Profile(user=user)
        
        self.assertEqual('Atticus', profile.get_full_name())
    
    def test_full_name_uses_first_and_last_name_when_present(self):
        user = User(username='testing', first_name='Atticus', last_name='Finch')
        profile = Profile(user=user)
        
        self.assertEqual('Atticus Finch', profile.get_full_name())
    
    def test_has_projects_false_when_no_projects(self):
        profile = Profile()
        
        self.assertFalse(profile.has_projects())
    
    def test_has_projects_true_when_at_least_one_project_present(self):
        profile = Profile(project_1_url='http://gatewayhackers.com')
        
        self.assertTrue(profile.has_projects())
    
    def test_has_elsewhere_false_when_no_elsewheres(self):
        profile = Profile()
        
        self.assertFalse(profile.has_elsewhere())
    
    def test_has_elswhere_true_when_at_least_one_elsewhere_present(self):
        profile = Profile(elsewhere_1_url='http://gatewayhackers.com')
        
        self.assertTrue(profile.has_elsewhere())

class ProfileDetailViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testing', first_name='Atticus', last_name='Finch')
    
    def sanity_check(self):
        response = self.client.get('/users/testing')
        
        self.assertContains(response, 'Atticus Finch')
