from django.conf.urls import patterns, url
from .views import NewsItemList


urlpatterns = patterns('',
    url(r'^$', NewsItemList.as_view(), name='news-index'),
)