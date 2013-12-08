from django.conf.urls import patterns, url, include
from .views import PostCreate, PostDetailView, PostListView, UserPostListView


urlpatterns = patterns('',
    url(r'^submit/$', PostCreate.as_view(), name='post-add'),
    url(r'^fetchtitle$', 'posts.views.fetch_url_title', name='fetch-url-title'),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='post-details'),
    url(r'^$', PostListView.as_view(), name='post-list'),
    url(r'^user/(?P<username>\w+)/$', UserPostListView.as_view(), name='user-post-list'),
)