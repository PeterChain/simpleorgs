from django.shortcuts import render
from django.views.generic import DetailView, CreateView

from .models import Member


class MemberCreate(CreateView):
    model = Member
    template_name = 'member/newmember.html'


class MemberDetail(DetailView):
    """
    View for displaying a member
    """
    template_name = 'member/memberdetail.html'
    model = Member
