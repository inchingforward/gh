from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .views import get_pages


class GetPagesViewTest(TestCase):
    def test_get_pages_returns_404_for_non_staff(self):
        response = self.client.get('/sources/')
        
        self.assertEqual(response.status_code, 404)
    
    def test_get_pages_returns_200_for_staff(self):
        request = RequestFactory().get('/sources/')
        request.user = User.objects.create(username='testing', is_staff=True)
        
        response = get_pages(request)
        
        self.assertEqual(response.status_code, 200)

