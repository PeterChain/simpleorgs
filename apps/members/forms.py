from django import forms

from django_countries.fields import LazyTypedChoiceField, countries

from .models import *
from apps.address.models import Address


class NewMemberForm(forms.Form):
    """
    Form for creating both new members and address
    """
    name = forms.CharField(max_length=45)
    surname = forms.CharField(max_length=45)
    date_of_birth = forms.DateField()
    email = forms.EmailField(required=False)
    telephone = forms.CharField(max_length=20, required=False)
    status = forms.ModelChoiceField(queryset=MemberStatus.objects.filter(initial_status=True))
    picture = forms.ImageField()
    nationality = LazyTypedChoiceField(choices=countries)

    # Address specific fields
    street = forms.CharField(max_length=50)
    house_no = forms.CharField(max_length=10)
    postal_code = forms.CharField(max_length=20)
    city = forms.CharField(max_length=80)
    state = forms.CharField(max_length=80)
    country = LazyTypedChoiceField(choices=countries)

    # Administrive task
    member_no = forms.CharField(max_length=5)
    generate_user = forms.BooleanField()

    
    