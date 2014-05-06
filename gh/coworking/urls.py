from django.conf.urls import patterns, url
from .views import CoworkingSpaceListView


urlpatterns = patterns('',
    url(r'^$', CoworkingSpaceListView.as_view(), name='coworking-spaces'),
)