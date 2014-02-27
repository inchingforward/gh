from django.test import TestCase
from django.contrib.auth.models import User
import views
from .models import Post


class PostListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testing')
        
    def test_post_list_view_contains_posts(self):
        Post.objects.create(title='Test Post', user=self.user)
        
        response = self.client.get('/posts/')
        
        self.assertContains(response, 'Test Post')
    
    def test_post_list_view_does_not_contain_hidden_posts(self):
        Post.objects.create(title='Visible Post', user=self.user)
        Post.objects.create(title='Hidden Post', user=self.user, visible=False)
        
        response = self.client.get('/posts/')
        
        self.assertContains(response, 'Visible Post')
        self.assertNotContains(response, 'Hidden Post')
    
    def test_post_list_view_paginates(self):
        for x in range(30):
            item = Post()
            item.title = 'Title %s' % x
            item.visible = True
            item.user = self.user
            item.save()
        
        response = self.client.get('/posts/')
        
        self.assertContains(response, 'Title 29')
        self.assertContains(response, 'Title 10')
        self.assertNotContains(response, 'Title 9')
        
        response = self.client.get('/posts/?page=2')
        
        self.assertContains(response, 'Title 9')
        self.assertContains(response, 'Title 0')

class PostDetailView(TestCase):
    def test_post_detail_view_sanity_test(self):
        user = User.objects.create(username='testing')
        
        post = Post.objects.create(title='Test Title', details='Test Details', user=user)
        
        response = self.client.get('/posts/%s/' % post.id)
        
        self.assertContains(response, 'Test Title')

class UserPostListViewTest(TestCase):
    def test_user_post_list_only_contains_posts_for_given_user(self):
        user1 = User.objects.create(username='user1')
        user2 = User.objects.create(username='user2')
        
        Post.objects.create(title='Test1', user=user1)
        Post.objects.create(title='Test2', user=user1)
        Post.objects.create(title='Test3', user=user2)
        
        response = self.client.get('/posts/user/user1/')
        
        self.assertContains(response, 'Test1')
        self.assertContains(response, 'Test2')
        self.assertNotContains(response, 'Test3')

