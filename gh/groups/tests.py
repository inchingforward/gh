from django.test import TestCase


class GroupsViewTest(TestCase):
    def test_groups_view_sanity(self):
        response = self.client.get('/groups/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Coming soon...')
