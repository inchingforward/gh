from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404
from braces.views import LoginRequiredMixin
from .models import Profile
from .forms import ProfileForm


class ProfileDetailView(DetailView):
    model = Profile
    
    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])

class ProfileUpdateView(LoginRequiredMixin,UpdateView):
    model = Profile
    form_class = ProfileForm
    
    def get_object(self):
        print self.kwargs
        print self.request.user
        try:
            return Profile.objects.get(user=self.request.user)
        except Profile.DoesNotExist:
            profile = Profile(user=self.request.user)
            profile.save()
            return profile
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProfileUpdateView, self).form_valid(form)
