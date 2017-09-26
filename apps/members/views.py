from django.shortcuts import render
from django.views.generic import DetailView, CreateView

from .models import Member
from .forms import NewMemberForm


class MemberCreate(CreateView):
    form_class = NewMemberForm
    template_name = 'members/newmember.html'

    


class MemberDetail(DetailView):
    """
    View for displaying a member
    """
    template_name = 'members/memberdetail.html'
    model = Member
