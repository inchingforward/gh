from django.conf import settings
from django.core.urlresolvers import reverse
from allauth.account.adapter import DefaultAccountAdapter
from profiles.models import Profile


class AccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        try:
            profile = Profile.objects.get(user=request.user)
            return reverse('index')
        except Profile.DoesNotExist:
            return reverse('profile-edit')
