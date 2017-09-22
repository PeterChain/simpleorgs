from django.forms import ModelForm

from .models import *


class MemberForm(ModelForm):
    """
    Model form for Member general information model
    """
    model = Member