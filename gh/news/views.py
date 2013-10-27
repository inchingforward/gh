from django.views.generic import ListView
from .models import NewsItem


class NewsItemList(ListView):
    model = NewsItem
