from django.forms import ModelForm

from .models import *


class AddressForm(ModelForm):
    """
    Model form for Member general information model
    """
    class Meta:
        model = Member
        exclude = ('slug', 'address_book')