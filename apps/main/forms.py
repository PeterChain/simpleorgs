from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """
    Form for validating credentials
    """
    username = forms.CharField(max_length=5,
        label=_("Username")
    )
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput()
    )

    def clean(self):
        """
        Validate the cleaned form
        """
        self.cleaned_data = super().clean()
        print(self.cleaned_data)
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        try:
            user = User.objects.get(username=username,
                                    is_active=True)

            try:
                self.authed_user = authenticate(
                    username=username,
                    password=password
                )

                if self.authed_user:
                    print("here perhaps?")
                    return self.cleaned_data

            except ValueError:
                print("error in authentication")
                self.authed_user = None

            if self.authed_user:
                return self.cleaned_data

        except (User.DoesNotExist, KeyError):
            print("Does not exist")
            pass

        raise forms.ValidationError("Your login details were incorrect. Please try again.")

    def get_user(self):
        """
        Return the authenticated user
        """
        return self.authed_user