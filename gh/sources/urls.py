from django.conf.urls import patterns, url, include
from .views import get_pages


urlpatterns = patterns('',
    url(r'^pages/$', get_pages, name='sources-pages'),
)