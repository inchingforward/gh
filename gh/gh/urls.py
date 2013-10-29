from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from .views import index


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^about/', TemplateView.as_view(template_name="about.html")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^news/', include('news.urls')),
    url(r'^posts/', include('posts.urls')),
    url(r'^profiles/', include('profiles.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
)
