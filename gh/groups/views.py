from django.shortcuts import render
from .models import Meetup


def meetups(request):
    meetups = Meetup.objects.all()
    return render(request, 'groups/meetups.html', {'meetups': meetups})
