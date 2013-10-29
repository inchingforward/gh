from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from .views import PostCreate, PostDetailView


urlpatterns = patterns('',
    url(r'^submit/$', login_required(PostCreate.as_view()), name='post-add'),
    url(r'^fetchtitle$', 'posts.views.fetch_url_title', name='fetch-url-title'),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='post-details'),
)