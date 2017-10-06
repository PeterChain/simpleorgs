from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """
    Form for validating credentials
    """
    username = forms.CharField(
        required=True,
        label=_("Username")
    )
    password = forms.CharField(
        label=_("Password"),
        required=True,
        widget=forms.PasswordInput()
    )

    def clean(self):
        """
        Validate the cleaned form
        """
        self.cleaned_data = super(LoginForm, self).clean()
        user = self.cleaned_data['username']
        passwd = self.cleaned_data['password']

        try:
            user = User.objects.get(username=user,
                                    is_active=True)

            try:
                self.authed_user = authenticate(
                    username=user,
                    password=passwd
                )

                if self.authed_user:
                    return self.cleaned_data

            except ValueError:
                self.authed_user = None

            if self.authed_user:
                return self.cleaned_data

        except (User.DoesNotExist, KeyError):
            pass

        raise forms.ValidationError("Your login details were incorrect. Please try again.")

    def get_user(self):
        """
        Return the authenticated user
        """
        return self.authed_user