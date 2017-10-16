from django import forms
from django.utils.translation import ugettext_lazy as _

from django_countries.fields import LazyTypedChoiceField, countries

from .models import *
from .utils import NumberRange
from apps.address.models import Address


class NewMemberForm(forms.Form):
    """
    Form for creating both new members and address
    """
    name = forms.CharField(max_length=45)
    surname = forms.CharField(max_length=45)
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type':'date'})
    )
    email = forms.EmailField(required=False)
    telephone = forms.CharField(max_length=20, required=False)
    status = forms.ModelChoiceField(queryset=MemberStatus.objects.filter(initial_status=True), required=False)
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
    member_no = forms.CharField(max_length=5, required=False)
    generate_user = forms.BooleanField(initial=False, required=False)

    def clean_postal_code(self):
        """
        Postal code is a mandatory for all addresses
        """
        postal_code = self.cleaned_data['postal_code']

        if not postal_code:
            raise forms.ValidationError(_("Postal code is required for address"))
        return postal_code
    
    def clean_generate_user(self):
        """
        If the member will have a user, email is required
        """
        generate_user = self.cleaned_data['generate_user']
        email = self.cleaned_data['email']

        if generate_user == True and not email:
            raise ValidationError(_("E-mail is required for user generation"))
        return generate_user

    def clean_member_no(self):
        """
        Validate member's No. uniqueness or gets a new one
        """
        member_no = self.cleaned_data['member_no']

        # If member No. is filled, we must check if it's unique
        if not member_no:
            if Member.objects.filter(member_no=member_no):
                raise forms.ValidationError(_("Member No. is already taken"))

            # If empty, we increment a unit to the last one
            if Member.objects.exists():
                max_no = Member.objects.all().aggregate(Max(member_no))
                if max_no:
                    num_range = NumberRange(max_no)
                else:
                    num_range = NumberRange("00000")
                member_no = num_range.next(1)

        return member_no
