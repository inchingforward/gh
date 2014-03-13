from django.conf.urls import patterns, url
from .views import meetups


urlpatterns = patterns('',
    url(r'meetups/$', meetups, name='meetups'),
)