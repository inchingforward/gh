from django.shortcuts import render
from .models import Meetup


def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'groups/index.html', {'meetups': meetups})
