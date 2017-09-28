from django.shortcuts import render
from django.forms import ChoiceField
from django.views.generic import DetailView, FormView

from .models import Member, MemberStatus
from .forms import NewMemberForm


class MemberCreate(FormView):
    """
    View for creating a complex form of member/address
    """
    form_class = NewMemberForm
    template_name = 'members/newmember.html'
    success_url = '/'

    def get_initial(self):
        """
        Default values for the member
        """
        initial = super(MemberCreate, self).get_initial()

        # Prepopulate member's status
        statuses = MemberStatus.objects.filter(initial_status=True)
        statuses_choices = []
        for status in statuses:
            statuses_choices.append(
                (status.status_code, status.status_text)
            )
        initial['status'] = ChoiceField(choices=statuses_choices)

        return initial


class MemberDetail(DetailView):
    """
    View for displaying a member
    """
    template_name = 'members/memberdetail.html'
    model = Member
