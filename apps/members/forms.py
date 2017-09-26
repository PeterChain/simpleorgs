from django.forms import ModelForm

from .models import *
from apps.address.models import address
from apps.address.forms import AddressForm


class MemberForm(ModelForm):
    """
    Model form for Member general information model
    """
    class Meta:
        model = Member
        exclude = ('slug', 'address_book')

MemberAddressFormset = inlineformset_factory(Member, Address,
                                            form=MemberForm,
                                            extra=1)