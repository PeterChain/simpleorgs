from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView
from django.utils.translation import ugettext_lazy as _

from utils.navigation import Navigation


class Homepage(TemplateView):
    """
    View class for the index page
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        """
        Returns the tile menu list
        """
        context = super(Homepage, self).get_context_data()
        navigation = Navigation()

        # Member management block
        context['member_nav'] = navigation.get_member_nav()
        return context


