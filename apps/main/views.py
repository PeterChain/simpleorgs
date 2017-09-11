from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from .models import Member


class Homepage(TemplateView):
    """
    View class for the index page
    """
    template_name = 'index.html'


class MemberDetail(DetailView):
    """
    View for displaying a member
    """
    template_name = 'member/memberdetail.html'
    model = Member
    
