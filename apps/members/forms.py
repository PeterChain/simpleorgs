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

    def is_valid(self):
        """
        Validate the form data
        """
        if self.generate_user == True and not self.email:
            raise ValidationError(_("E-mail is required for user generation"))

        if not self.postal_code:
            raise ValidationError(_("Postal code is required for address"))

        # If member No. is filled, we must check if it's unique
        if not self.member_no:
            if Member.objects.filter(slug=self.member_no):
                raise ValidationError(_("Member No. is already taken"))

            # If empty, we increment a unit to the last one
            if Member.objects.exists():
                max_no = Member.objects.all().aggregate(Max(member_no))
                if max_no:
                    num_range = NumberRange(max_no)
                else:
                    num_range = NumberRange("00000")
                self.member_no = num_range.next(1)

        return True