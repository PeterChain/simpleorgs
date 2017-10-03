from django.views.generic.base import ContextMixin
from django.urls import reverse
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth.models import User

class LoggedProfileMixin(object):
    """
    Mixin for providing logged user information
    """
    def get_logged_profile(self):
        profile = {}

        if notself.request.user:
            return None

        try:
            member = Member.objects.get(
                member_no=self.request.user.username
            )

            profile.name = member.name
            profile.surname = member.surname
            profile.picture = member.picture
            profile.member_no = member.member_no
        except Member.DoesNotExist:
            return None

        return context



class UserAuthMixin(object):
    """
    Mixin for checking access to restricted areas
    """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            # return HttpResponseForbidden()
            return HttpResponseRedirect(reverse('login'))
        return super(UserAuthMixin, self).dispatch(request, *args, **kwargs)

