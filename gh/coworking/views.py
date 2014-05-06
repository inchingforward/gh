from django.views.generic.list import ListView
from .models import CoworkingSpace


class CoworkingSpaceListView(ListView):
    model = CoworkingSpace
