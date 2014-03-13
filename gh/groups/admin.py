from django.contrib import admin
from .models import Meetup, MeetupEvent


admin.site.register(Meetup)
admin.site.register(MeetupEvent)
