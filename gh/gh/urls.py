from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from posts.views import PostListView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', PostListView.as_view(), name='index'),
    url(r'^about/', TemplateView.as_view(template_name="about.html")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^news/', include('news.urls')),
    url(r'^posts/', include('posts.urls')),
    url(r'^profiles/', include('profiles.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    (r'^accounts/', include('allauth.urls')),
)
