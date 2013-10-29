from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from .views import PostCreate


urlpatterns = patterns('',
    url(r'^submit/$', login_required(PostCreate.as_view()), name='post-add'),
    url(r'^fetchtitle$', 'posts.views.fetch_url_title', name='fetch-url-title'),
)