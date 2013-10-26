from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    (r'^$', TemplateView.as_view(template_name="index.html")),
    (r'^about/', TemplateView.as_view(template_name="about.html")),
    
    url(r'^admin/', include(admin.site.urls)),
)
