from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import TemplateView, FormView, View, UpdateView
from django.utils.translation import ugettext_lazy as _

from utils.navigation import Navigation

from .forms import LoginForm, SettingsForm
from .mixin import UserAuthMixin


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        """
        Redirects to homepage if it's already logged
        """
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        """
        Creates the logged session
        """
        user = form.get_user()
        session_key = self.request.session.session_key
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """
        Returns the error messages to the user
        """
        messages.add_message(
            self.request, messages.ERROR, _("The credentials don't match any account")
        )
        return super().form_invalid(form)

    def get_success_url(self):
        """
        Returns URL for index
        """
        return reverse('homepage')


class LogoutView(View):
    """
    View for logout the user and end the session
    """
    def get(self, request, *args, **kwargs):
        """
        Redirects to homepage if it's already logged
        """
        if request.user.is_authenticated():
            logout(request)
            return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        """
        returns the URL for the login page
        """
        return reverse('login')


class Homepage(UserAuthMixin, TemplateView):
    """
    View class for the index page
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        """
        Returns the tile menu list
        """
        context = super(Homepage, self).get_context_data()
        navigation = Navigation()

        # Member management block
        context['member_nav'] = navigation.get_member_nav()
        return context


class UserSettingsView(UpdateView):
    """
    View for updating user specific information
    """
    form_class = SettingsForm
    template_name = 'settings.html'

    def get_success_url(self):
        """
        Returns the homepage as successful change
        """
        return reverse('homepage')

    def get_object(self):
        """
        Returns the User object of the session
        """
        return self.request.user

    def form_valid(self, form):
        user = self.request.user
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super(UserSettingsView, self).form_valid(form)