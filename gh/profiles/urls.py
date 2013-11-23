from django.conf.urls import patterns, url
from .views import ProfileDetailView, ProfileUpdateView


urlpatterns = patterns('',
    url(r'^edit/$', ProfileUpdateView.as_view(), name='profile-edit'),
    url(r'^(?P<username>\w+)/$', ProfileDetailView.as_view(), name='profile-detail'),
)