from django.test import TestCase
from django.test import RequestFactory
from django.contrib.auth.models import User
from .models import Profile
from .views import ProfileDetailView


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
        self.profile = Profile.objects.create(user=self.user)
    
    def test_profile_detail_contains_full_name(self):
        response = self.client.get('/profiles/testing/')
        
        self.assertContains(response, 'Atticus Finch')
    
    def test_edit_button_present_for_users_own_profile(self):
        request = RequestFactory().get('/profiles/testing/')
        request.user = self.user
        
        response = ProfileDetailView.as_view()(request, username=self.user.username)
        
        self.assertContains(response, 'Edit')
    
    def test_edit_button_not_present_for_other_users_profile(self):
        request = RequestFactory().get('/profiles/testing/')
        
        response = ProfileDetailView.as_view()(request, username=self.user.username)
        
        self.assertNotContains(response, 'Edit')

