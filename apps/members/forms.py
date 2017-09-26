from django import forms

from django_countries.fields import LazyTypedChoiceField

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
    status = forms.ModelChoiceField(queryset=None)
    picture = models.ImageField()
    nationality = LazyTypedChoiceField()

    # Address specific fields
    street = models.CharField(max_length=50)
    house_no = models.CharField(max_length=10)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=80)
    state = models.CharField(max_length=80)
    country = LazyTypedChoiceField()

    # Administrive task
    member_no = models.CharField(max_length=5)
    generate_user = models.BooleanField(default="X")

    def __init__(self, **kwargs):
        super(NewMemberForm, self).__init__(*args, **kwargs)

        self.fields['status'] = Member.status.all()