from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from .models import Profile


class ProfileDetailView(DetailView):
    model = Profile
    
    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])
